import requests
import json
import constant
from stackoverflow_item import *
from github_item import *


class ApiCall:
    def __init__(self, api_source):
        self.api_source = api_source

    def call(api_source):
        api_item = ""
        if api_source == 'so':
            # response = requests.get('https://api.stackexchange.com/users/3485221/answers?site=stackoverflow')
            response = requests.get('https://api.stackexchange.com/users/3485221/reputation-history?site=stackoverflow')
            parsed_response = json.loads(response.text)
            # api_item = StackOverflowItem() # to do next
        elif api_source == 'github':
            response = requests.get(constant.GITHUB_API + constant.GITHUB_USER_EVENTS)
            parsed_response = json.loads(response.text)        
            # temporaly it only extracts first item from the parsed json response, todo, extract all the events into objects and append them to event class    
            api_item = GithubItem(parsed_response[0]['type'], parsed_response[0]['payload']) 
            
        return api_item

