#
# class ApiCall -> return json -> parse json -> create an event list item
#
from apicall import *
import pprint

# so = ApiCall.call('so')
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(so)

gh = ApiCall.call('github')
pp = pprint.PrettyPrinter(indent=4)
pp.print(gh)