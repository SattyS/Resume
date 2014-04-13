import json
from pprint import pprint
json_data=open('2012-04-11-15.json')

data = json.load(json_data)
pprint(data)
json_data.close()