# class ApiCall -> return json -> parse json -> create an event list item
# from test import Event
# import requests
# import json

# API_URL = 'https://api.github.com'

# response = requests.get( API_URL + '/users/ltx-dev/events')
# parsed_response = json.loads(response.text) # loads deserializes json

# actor = parsed_response[0]['actor']
# type1 = parsed_response[0]['type']
# created_at = parsed_response[0]['created_at']

# event1 = Event(actor, type1, created_at)
# event_list = []    

# for element in parsed_response:
#     event_list.append(Event(element['actor'], element['type'], element['created_at']))

# print(event_list)

from apicall import *
import pprint

so = ApiCall.call('so')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(so)
