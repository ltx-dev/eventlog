import requests

class ApiCall:
    def __init__(self, api_source):
        self.api_source = api_source

    GITHUB_API = 'https://api.github.com'
    GITHUB_USER_EVENTS = '/users/ltx-dev/events' # events from my own repo for the time being
    # STACKEXCHANGE API ADDRESS GOES HERE
    STACKEXCHANGE_NETWORK_ACTIVITY = '/users/3485221/network-activity' # my own user id

    def call(self.api_source):
            