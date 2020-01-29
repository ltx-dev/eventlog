# get last and/or list of events on user's github profile

# api request > get json > parse json = json response is now a dictionary
import requests
import json
import pprint

API_URL = 'https://api.github.com'

response = requests.get( API_URL + '/users/ltx-dev/events')
parsed_response = json.loads(response.text) # loads deserializes json

pp = pprint.PrettyPrinter(indent=4)

class Event:
    def __init__(self, actor, type, created_at):
        self.actor = actor
        self.type = type
        self.created_at = created_at

actor = parsed_response[0]['actor']
type1 = parsed_response[0]['type']
created_at = parsed_response[0]['created_at']

event1 = Event(actor, type1, created_at)
event_list = []    

for element in parsed_response:
    event_list.append(Event(element['actor'], element['type'], element['created_at']))

print(event_list.type)

# print(event1.actor)
# print(event1.type)
# print(event1.created_at)