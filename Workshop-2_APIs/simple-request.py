#
#  Date:  Oct 13 2020
#  File:  simple-request.py
#  Auth:  Monica Ihli monica@utk.edu

import requests
import xml.etree.ElementTree as ET
url = "http://volweb.utk.edu/~mihli1/demos/case1.xml"

r = requests.get(url) # assign what is returned from GET request to a response object called r
if r.status_code == 200:
  print("Successfully fetched " + url)
  print(r.content)
  # XML
  xml_data = ET.fromstring(r.content)  # plug the returned XML content straight into ElementTree
  # remember, these variables are examples of data being stored in memory. We have
  # NOT written anything to permanent storage yet by writing to a file

  #display one element a time
  for elem in xml_data:  # for every child node within root (cookies, pies)
    print(elem.tag)  # print the element name. This first level of child nodes also has no text
    for subelement in elem:  # for all the subelements in the next level down
      print(subelement.tag, subelement.text)  # print the tag and the text, since these have text




