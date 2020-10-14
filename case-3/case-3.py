#
#  Date:  Oct 13 2020
#  File:  case-3.py
#  Auth:  Monica Ihli monica@utk.edu


import requests
from bs4 import BeautifulSoup # this handles parsing data from html content

url = "http://volweb.utk.edu/~mihli1/demos/case3.html"
response = requests.get(url)
soup = BeautifulSoup(response.content,
                     "html.parser")

for child in soup.children:
  print(child)  # will print ALL the children of the top-level document

print('\n')

# search by tag
paragraphs = soup.find_all('p')  # find every html element with a P tag. returns a ResultSet (like a list) of tags
for p in paragraphs:  # iterate over all the tags in the set of results
  print(p.text)  # print the text of the current tag
  if p.b:  # if searching for a <b> tag inside the current <p> doesn't return None
    print("{} is in BOLD!".format(p.b))  # then print something

print(soup.p)  # print just the first p soup finds