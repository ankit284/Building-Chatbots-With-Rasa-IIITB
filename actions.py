from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot

import zomatopy
import json
from flask import Flask
from flask_mail import Message, Mail
import app_email
import ast
import config_loader


class ActionSearchRestaurants(Action):
        
        def name(self):
                return 'action_restaurant'
        
        def run(self, dispatcher, tracker, domain):
                config={ "user_key":config_loader.get_zomato_config()}
                zomato = zomatopy.initialize_app(config)
                loc = tracker.get_slot('location')
                budget=tracker.get_slot('budget')
                cuisine = tracker.get_slot('cuisine')
                if loc!=None:
                        if Validation_Utilities().ValidateLocation(dispatcher,tracker)==False:
                                dispatcher.utter_template('utter_noService',tracker)
                                return [SlotSet('location',None)]
                        elif cuisine==None:
                                dispatcher.utter_template('utter_ask_cuisine',tracker)
                                return [SlotSet('location',tracker.get_slot('location'))]
                else:
                        dispatcher.utter_template('utter_ask_location',tracker)
                        return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('budget',budget)]
                if cuisine!=None:
                        if Validation_Utilities().ValidateCuisine(dispatcher,tracker)==False:
                                dispatcher.utter_template('utter_ask_cuisine',tracker)
                                return [SlotSet('cuisine',None)]
                        elif budget==None:
                                dispatcher.utter_template('utter_ask_budget',tracker)
                                return [SlotSet('cuisine',tracker.get_slot('cuisine'))]
                else:
                        dispatcher.utter_template('utter_ask_cuisine',tracker)
                        return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('budget',budget)]
                if budget==None:
                        dispatcher.utter_template('utter_ask_budget',tracker)
                        return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('budget',budget)]
                if cuisine!=None and loc!=None and budget!=None:
                        
                        location_detail=zomato.get_location(loc, 1)                
                        d1 = json.loads(location_detail)
                                
                        lat=d1["location_suggestions"][0]["latitude"]
                        lon=d1["location_suggestions"][0]["longitude"]
                        city_id=d1["location_suggestions"][0]["city_id"]
                        tracker.update(SlotSet("lat",lat))
                        tracker.update(SlotSet("lon",lon))
                        tracker.update(SlotSet("city_id",city_id))
                   
                        cuisine_details=zomato.get_cuisines(city_id)
                        cuisine_key=""
                        try:
                                c_k=list(cuisine_details.keys())
                                c_v=list(cuisine_details.values())
                                c_v=[x.lower() for x in c_v]
                                c_index=c_v.index(cuisine.lower())
                                cuisine_key=str(c_k[c_index])
                                tracker.update(SlotSet('cuisine_key',cuisine_key))
                        except ValueError as e:
                                dispatcher.utter_message("Sorry! not able to find cuisine {} restaurant. Please choose another cuisine".format(cuisine))
                                dispatcher.utter_template('utter_ask_cuisine',tracker)
                                return [SlotSet('cuisine',None)]
                        if cuisine_key!='':       
                                results=zomato.restaurant_search("", lat, lon, cuisine_key, 10)
                                d = json.loads(results)
                                api_response="{"
                                response=""
                                if d['results_found'] == 0:
                                        response= "no results"
                                else:
                                        counter=1
                                        for restaurant in d['restaurants']:
                                                api_response+='"{}":["{}","{}","{}","{}"]'.format(counter,restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],restaurant['restaurant']['user_rating']['aggregate_rating'])
                                                if counter<6:
                                                        response=response+ str(counter)+" : "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating'] +"\n"
                                                if counter<10:
                                                        api_response+=","
                                                        counter+=1
                                api_response+="}"
                                tracker.update(SlotSet('api_response',api_response))
                                dispatcher.utter_message("-----\n"+response)
                                return [SlotSet('location',loc),SlotSet('api_response',api_response),SlotSet('budget',budget),SlotSet('cuisine',cuisine)]
                        else:
                                dispatcher.utter_template('utter_ask_cuisine',tracker)
                                return [SlotSet('location',loc),SlotSet('cuisine',None),SlotSet('budget',budget)]
        
class ActionGoodBye(Action):
        def name(self):
                return 'action_goodbye'
        def run(self, dispatcher, tracker, domain):
                return [SlotSet('location',None),SlotSet('api_response',None),SlotSet('cuisine',None),SlotSet('budget',None)]

class ActionSendEmail(Action):
        def name(self):
                return 'action_send_email'

        def run(self, dispatcher, tracker, domain):
                response="No Success"
                email_id=tracker.get_slot('email')
                sendermail=str(email_id).split('|')[-1]
                email_id=sendermail
                cuisine_id=tracker.get_slot('cuisine')
                location_id=tracker.get_slot('location')
                response_var=str(tracker.get_slot('api_response'))
                filtered_text=response_var
                replace_expression=["'","\n","\t","\s"]
                for replacement in replace_expression:
                        filtered_text=filtered_text.replace(replacement," ")
                response_var=filtered_text
                render_html=True
                try:
                        api_response=ast.literal_eval(response_var)
                        response=app_email.send_mail("Top 10",str(cuisine_id) + " restaurants in "+location_id +".",api_response,email_id,render_html)
                except:
                        render_html=False

                if response != "Success":
                        dispatcher.utter_template('utter_email_not_sent', tracker)
                else:
                        dispatcher.utter_template('utter_email_sent', tracker)
                return [SlotSet('email',None),SlotSet('location',None),SlotSet('cuisine',None),SlotSet('budget',None)]

class Validation_Utilities():
        def ValidateLocation(self, dispatcher, tracker):
                validation_status=True
                loc = tracker.get_slot('location')
                if loc!=None:
                        with open('./data/lookup/syn_location.json') as json_file:
                                json_loc=json.load(json_file)
                        if json_loc.get(str(loc).lower())!=None:
                                loc_value=json_loc.get(str(loc).lower())
                                loc=loc_value
                                tracker.update(SlotSet("location",loc_value))
                        with open('./data/lookup/locations.txt','r') as lookup:
                                city_lookuplist=lookup.read().splitlines()
                                city_lookuplist=[x.lower() for x in city_lookuplist]
                        
                        if loc not in city_lookuplist:
                                        validation_status= False
                        else:
                                validation_status=True
                else:
                        validation_status=False
                return validation_status
        
        def ValidateCuisine(self,dispatcher,tracker):
                cuisine = tracker.get_slot('cuisine')
                validation_status=True
                if cuisine!=None:
                        with open('./data/lookup/syn_cuisine.json') as json_file:
                                json_cusine=json.load(json_file)
                        if json_cusine.get(str(cuisine).lower())!=None:
                                cuisine_val=json_cusine.get(str(cuisine).lower())
                                tracker.update(SlotSet("cuisine",cuisine_val))
                        else:
                                validation_status=False
                else:
                        validation_status=False
                return validation_status
