import requests
import json

class ApiCall:
    def __init__(self, api_source):
        self.api_source = api_source

    GITHUB_API = 'https://api.github.com'
    GITHUB_USER_EVENTS = '/users/ltx-dev/events' # events from my own repo for the time being
    STACKEXCHANGE_API = 'https://api.stackexchange.com/'
    STACKEXCHANGE_NETWORK_ACTIVITY = '/users/3485221/network-activity' # my own user id

    def call(api_source):
        if api_source == 'so':
            response = requests.get('https://api.stackexchange.com/users/3485221/answers?site=stackoverflow')
            parsed_response = json.loads(response.text)
        
        return parsed_response            

            