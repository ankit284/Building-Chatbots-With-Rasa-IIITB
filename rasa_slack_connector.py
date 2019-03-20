from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import json

from builtins import str
from flask import Blueprint, request, jsonify, make_response, Response

from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent
from slackclient import SlackClient
logger = logging.getLogger(__name__)


class SlackBot(OutputChannel):

	@classmethod
	def name(cls):
		return "slack"
	def __init__(self, slack_verification_token, channel):
		self.slack_verification_token = slack_verification_token
		self.channel = channel
		
	def send_text_message(self, recipient_id, message):
		text = message
		recipient = recipient_id
		
		CLIENT = SlackClient(self.slack_verification_token)
		CLIENT.api_call('chat.postMessage', channel = self.channel, text = text, as_user = True)
	
	@staticmethod
	def _convert_to_slack_buttons(buttons):
		return [{"text": b['title'],"name": b['payload'],"type": "button"} for b in buttons]
	
	def send_text_with_buttons(self, recipient_id, message, buttons, **kwargs):
		recipient = self.channel or recipient_id
		
		if len(buttons) > 6:
			logger.warning("Slack API currently allows only up to 5 buttons. "
						"If you add more, all will be ignored.")
			return self.send_text_message(recipient, message)

		button_attachment = [{"fallback": message,
								"callback_id": message.replace(' ', '_')[:20],
								"actions": self._convert_to_slack_buttons(
										buttons)}]
		CLIENT = SlackClient(self.slack_verification_token)

		CLIENT.api_call("chat.postMessage",channel=recipient,as_user=True,text=message,attachments=button_attachment)



class SlackInput(HttpInputComponent):
	def __init__(self, slack_dev_token, slack_verification_token, slack_client, debug_mode):
		self.slack_dev_token = slack_dev_token
		self.debug_mode = debug_mode
		self.slack_client = slack_client
		self.slack_verification_token = slack_verification_token
		self.errors_ignore_retry = ('http_timeout',)
		
	@staticmethod
	def _is_user_message(slack_event):
		return (slack_event.get('event') and
				slack_event.get('event').get('type') == u'message' and
				slack_event.get('event').get('text') and not
				slack_event.get('event').get('bot_id'))

	@staticmethod
	def _is_button_reply(slack_event):
		return (slack_event.get('payload') and
				slack_event['payload'][0] and
				'name' in slack_event['payload'][0])

	@staticmethod
	def _get_button_reply(slack_event):
		return json.loads(slack_event['payload'][0])['actions'][0]['name']

	def process_message(self, on_new_message, text, sender_id):
		retry_reason = request.headers.environ.get('HTTP_X_SLACK_RETRY_REASON')
		retry_count = request.headers.environ.get('HTTP_X_SLACK_RETRY_NUM')
		if retry_count and retry_reason in self.errors_ignore_retry:
			logger.warning("Received retry #{} request from slack due to {}".format(retry_count, retry_reason))
			return Response(status=201, headers={'X-Slack-No-Retry': 1})
		try:
			out_channel = SlackBot(self.slack_verification_token,self.channel)
			user_msg = UserMessage(text, SlackBot(self.slack_verification_token, self.channel))
			on_new_message(user_msg)
		except Exception as e:
			logger.error("Exception when trying to handle "
							"message.{0}".format(e))
			logger.error(str(e), exc_info=True)

		return make_response()

	def blueprint(self, on_new_message):
		from flask import Flask, request, Response
		slack_webhook = Blueprint('slack_webhook', __name__)
		
		@slack_webhook.route('/', methods = ['GET'])
		def health():
			return jsonify({'status':'ok'})
		
		@slack_webhook.route("/webhook", methods=['POST'])
		def webhook():
			request.get_data()
			if request.json:
				output = request.json
				if "challenge" in output:
					return make_response(output.get("challenge"), 200,
											{"content_type": "application/json"})
				elif self._is_user_message(output):
					return self.process_message(
							on_new_message,
							text=output['event']['text'],
							sender_id=output.get('event').get('user'))
			elif request.form:
				output = dict(request.form)
				if self._is_button_reply(output):
					return self.process_message(
							on_new_message,
							text=self._get_button_reply(output),
							sender_id=json.loads(
									output['payload'][0]).get('user').get(
								'id'))
			return make_response()

		@slack_webhook.route('/slack/events', methods = ['POST'])
		def event():
			if request.json.get('type') == 'url_verification':
				return request.json.get('challenge'), 200
				
			if request.json.get('token') == self.slack_client and request.json.get('type') == 'event_callback':
				data = request.json
				messaging_events = data.get('event')
				self.channel = messaging_events.get('channel')
				user = messaging_events.get('user')
				text = messaging_events.get('text')
				bot = messaging_events.get('bot_id')
				if bot == None:
					on_new_message(UserMessage(text, SlackBot(self.slack_verification_token, self.channel)))
					
			return Response(), 200
			
		return slack_webhook
				
		
		
		
		
