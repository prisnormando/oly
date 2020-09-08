import http.client, urllib.parse, time, sys
import json
from json import decoder
import secret_keys.config as config

#.config.py
#from secret_keys import config
# Represents the various elements used to create HTTP request URIs
# for QnA Maker operations.
# From Publish Page
host = config.HOST

# Authorization endpoint key
# From Publish Page
endpoint_key = config.ENDPOINT_KEY

# Management APIs postpend the version to the route
# From Publish Page
route = config.ROUTE

# JSON format for passing question to service
question = "{'question': 'What happens after 12 months?'}";

# Add post request
headers = {
    'Authorization': 'EndpointKey ' + endpoint_key,
    'Content-Type': 'application/json'
  }

try:
  conn = http.client.HTTPSConnection(host,port=443)
  conn.request ("POST", route,  question, headers)
  response = conn.getresponse ()
  answer = response.read ()
  print(json.dumps(json.loads(answer), indent=4))

except :
    print ("Unexpected error:", sys.exc_info()[0])
    print ("Unexpected error:", sys.exc_info()[1])