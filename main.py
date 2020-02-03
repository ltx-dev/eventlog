from apicall import *
import pprint

# so = ApiCall.call('so')
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(so)

gh = ApiCall.call('github')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(gh)

