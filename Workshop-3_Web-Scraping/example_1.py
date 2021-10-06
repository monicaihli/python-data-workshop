#
#  Date:  Oct 5 2021
#  File:  example_1.py
#  Auth:  Monica Ihli monica@utk.edu
#
#  This script corresponds with example.html, a test web page which demonstrates javascript can add content to a page
#  after the initial page load is complete. In this case, the extra content is added by the action of a user clicking
#  a button. So we intentionally know that this script will NOT capture all the sample data.
#
# This script demonstrates the limitations of the requests library, in that the library cannot interact with the page
# or execute javascript.
#
# Note: If using the accompanying html page as a file on disk instead of requesting over the internet, modify the code
# so that bs4 is loading the data from the file instead of a request.
#

import requests
from bs4 import BeautifulSoup # parses the HTML

example_url = "http://volweb.utk.edu/~mihli1/demos/case4.html"
headers = {'User-Agent': 'My Teaching Test App','From': 'monica@utk.edu'} # a dictionary of key-value pairs for headers
r = requests.get(example_url) # assign what is returned from GET request to a response object called r
if r.status_code == 200:
    # parsing with BS4
    soup = BeautifulSoup(r.content, "html.parser")  # load the page source into a soup object
    list_items = soup.find_all('li')  # find all the list items on this page

    for item in list_items:
        print(item.text)


