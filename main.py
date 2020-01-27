# get last and/or list of events on user's github profile

# test api request
# save the result to json
# use that to display the events on html
# Test how to parse it into objects

import requests
import json

API_URL = 'https://api.github.com'

response = requests.get( API_URL + '/users/ltx-dev/events')
parsed_response = json.loads(response.text)

print(json.dumps(parsed_response, indent=4, sort_keys=True))
print(parsed_response[2]['type'])
print(parsed_response[2]['actor']['url'])


# class Test(object):
# 	def __init__(self, data):
# 		self.__dict__ = json.loads(data)


# test1 = Test(parsed_response[0])
# print(test1.actor)
