########################################################################################################################
# File: xml_parser_2.py
# Author: Monica Ihli
# Date: 9/22/2021

# Description: Demonstrates reading XML data stored as a string in memory (in other words, from a variable). This
#              is a slightly different workflow where we use a third party library called requests to fetch the file
#              from a web server, and store the HTTP response in a variable. The content is then accessed as a string
#              property of that variable.
# Documentation for ElementTree module: https://docs.python.org/3/library/xml.etree.elementtree.html
########################################################################################################################

import requests # MUST INSTALL! Not standard library!
import xml.etree.ElementTree as ET

url = "http://volweb.utk.edu/~mihli1/demos/case1.xml"

r = requests.get(url) # assign what is returned from GET request to a response object called r
if r.status_code == 200:
  print("Successfully fetched " + url)
  print(r.text)
  # XML
  xml_data = ET.fromstring(r.text)  # plug the returned XML content straight into ElementTree
  # remember, these variables are examples of data being stored in memory. We have
  # NOT written anything to permanent storage yet by writing to a file

  #display one element a time
  for elem in xml_data:  # for every child node within root (cookies, pies)
    print(elem.tag)  # print the element name. This first level of child nodes also has no text
    for subelement in elem:  # for all the subelements in the next level down
      print(subelement.tag, subelement.text)  # print the tag and the text, since these have text