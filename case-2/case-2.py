#
#  Date:  Oct 13 2020
#  File:  case-2.py (NASA Near Earth Object API)
#  Auth:  Monica Ihli monica@utk.edu
#
#  Generate a free API key for NASA apis from https://api.nasa.gov/
#
#  Put the key in apikey.txt with nothing else. This is a good strategy for making sure you don't
#  accidently expose your private key, such as when you upload your latest code to github or share with a friend
#  because you can exclude the file with the API key from what you upload/share
#

#  NASA describes this API as "NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth
#  Asteroid information. With NeoWs a user can: search for Asteroids based on their closest approach date to
#  Earth, lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set."
# example https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY


import requests
import json  # the NASA api's respond with json, so you get to see a demo of this too.
# JSON is a machine readable format structured similarly to XML in many ways

# setup the URL part
base_url = "https://api.nasa.gov/neo/rest/v1/"
endpoint = "feed"


# setup query parameters.
start = "2020-10-01"
end = "2020-10-01"
with open('apikey.txt', 'r') as keyfile:
  apikey = keyfile.read()


# build and execute the request using the base URL, plus endpoint, plus query parameters
url = base_url + endpoint
query_params = {"start_date": start, "end_date": end, "api_key": apikey}
response = requests.get(url=url, params=query_params)

print("Now fetching: " + response.url) # print the URL that ultimately got constructed and requested

if response.status_code == 200:
  print('Success')
  response_string = json.loads(response.text) # load the string version of the response to a json object
  print(json.dumps(response_string, indent=2))

  # some things to watch out for with this response:
  # - notice that the first element is called links, and it tells you the URL for what comes before and what comes after
  # - notice the "element_count" tells you the count of how many objects matched your query
  # - notice that there are IDs / NEO reference IDs -- This API has another endpoint that will let you fetch full records
  #   by retrieving the record based on ID number


