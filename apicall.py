import requests
import json
import constant

class ApiCall:
    def __init__(self, api_source):
        self.api_source = api_source

    def call(api_source):
        if api_source == 'so':
            response = requests.get('https://api.stackexchange.com/users/3485221/answers?site=stackoverflow')
            parsed_response = json.loads(response.text)
        elif api_source == 'github':
            response = requests.get(constant.GITHUB_API + constant.GITHUB_USER_EVENTS)
            parsed_response = json.loads(response.text)            
        
        return parsed_response # create particular object here, eg if api_source == 'so' -> return StackOverflowItem object         

