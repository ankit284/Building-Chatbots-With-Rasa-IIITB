from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import warnings
import config_loader
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

config_status=config_loader.validate_application_config()
if config_status[0]:
	input_channel = SlackInput(config_loader.get_slack_config()['app_ver_token'], #app verification token
							config_loader.get_slack_config()['bot_ver_token'], # bot verification token
							config_loader.get_slack_config()['slack_ver_token'], # slack verification token
							True)
	agent.handle_channel(HttpInputChannel(5014, '/', input_channel))
else:
	print(config_status[1])