#
# Github contants
#
GITHUB_API = 'https://api.github.com'
GITHUB_USER_EVENTS = '/users/ltx-dev/events' # events from my own repo for the time being
STACKEXCHANGE_API = 'https://api.stackexchange.com/'
#
# Stackexchange (Stackoverflow) constants
#
SO_USER_ID = '3485221'
SE_WEBSITE_QUERY = '?site=stackoverflow'
SE_POSTS = "users/" + SO_USER_ID + "/posts" + SE_WEBSITE_QUERY + "&withbody" # posts = both answers and questions
SE_ANSWERS = "users/" + SO_USER_ID + "/answers" + SE_WEBSITE_QUERY
SE_QUESTIONS = "users/" + SO_USER_ID + "/questions" + SE_WEBSITE_QUERY
SE_NETWORK_ACTIVITY = 'users/' + SO_USER_ID + "/network-activity" # my own user id
