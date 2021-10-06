#
#  Date:  Oct 5 2021
#  File:  example_2.py
#  Auth:  Monica Ihli monica@utk.edu
#
#  This script corresponds with example.html, a test web page which demonstrates javascript can add content to a page
#  after the initial page load is complete. This is an example of when you would use selenium + chromedriver to interact
#  with the page or wait for javascript to load more content before going in and scraping the page source code with
#  beautiful soup
#
# Note: If using the accompanying html page as a file on disk instead of requesting over the internet, modify the code
# so that bs4 is loading the data from the file instead of the driver.
#

from selenium import webdriver # controls the webdriver application
from bs4 import BeautifulSoup # parses the HTML

# set up selenium
example_url = "http://volweb.utk.edu/~mihli1/demos/case4.html"
# must include path to where you downloaded the chromedriver:
driver = webdriver.Chrome(executable_path="/home/monica/Downloads/chromedriver")
driver.get(example_url)

# interact with the page using chromedriver to add content that is missing at the time of initial page load
button = driver.find_element_by_id("btnAdd") # inspect the page and figure out the identifying information of element
button.click() # click that button to execute functionality of adding an item to the list
print("Added items!")

# Experiment! What happens when you comment out the lines clicking the button?

# parsing with BS4
soup = BeautifulSoup(driver.page_source, "html.parser") # load the page source into a soup object
list_items = soup.find_all('li') # find all the list items on this page

for item in list_items:
  print(item.text)



