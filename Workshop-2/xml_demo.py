#
#  File:  xml_demo.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates parsing XML from demo-xml.xml
#                                    __________
#                                   [  snacks  ]
#                                        |
#                  ______________________|___________________
#                  |                                        |
#              ____|_____                               ____|_____
#             [  cookies ]                             [   pies   ]
#                  |                                        |
#     _____________|_____________               ____________|_____________
#     |            |            |              |            |            |
# ____|_____   ____|_____  _____|_____     ____|_____   ____|_____   ____|_____
#[  cookie  ] [  cookie  ] [  cookie  ]   [   pie    ] [   pie    ] [   pie    ]
#
################################################################################################################

import xml.etree.ElementTree as ET # the as part creates an alias, just optional convenience ("ET" is shorter to type)

################################################################################################################
# ITERABLE METHOD: Iterate over every child using for loops.
################################################################################################################
print("\nITERABLE SEARCH:")
tree = ET.parse("demo-xml.xml") # load the xml contents of file into memory as a full tree structure
root = tree.getroot() # get the root element, which is snack
print(root.tag) # print the tag name (snacks). It doesn't have any text to print.
for elem in root: # for every child node within root (cookies, pies)
  print(elem.tag) # print the element name. This first level of child nodes also has no text
  for subelement in elem: # for all the subelements in the next level down
    print(subelement.tag, subelement.text) # print the tag and the text, since these have text

################################################################################################################
# SEARCH & DRILL-DOWN WITH .FIND()/.FINDALL(): Allows pattern-matched searching, but only for immediate children.
################################################################################################################
print("\nSEARCH WITH METHODS:")
import xml.etree.ElementTree as ET
tree = ET.parse("demo-xml.xml")
root = tree.getroot()
print(root.tag)
pies_node = root.find("pies") # get the node which is called "pies"
print("\t" + pies_node.tag) # print  that node's tag name
pie_node_list = pies_node.findall("pie") # now find all child nodes within pies which are called "pie"
for pie in pie_node_list:
  print("\t\t" + pie.text)  # for every node in that list, print off the text it contains

# or the short version
tree = ET.parse("demo-xml.xml")
root = tree.getroot()
pie_node_list = root.find("pies").findall("pie") # find every node called "pie" inside a node called "pies"
for pie in pie_node_list:
  print(pie.text)



################################################################################################################
# SEARCH WITH XPATH: Allows more direct navigation to elements that match pattern. Do not have to move
# sequentially through the hierarchy.
# xpath syntax: https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax
################################################################################################################
print("\nSEARCH WITH XPATH:")

tree = ET.parse("demo-xml.xml")
root = tree.getroot()

# return a list of all pie children of pies and grandchildren of root node
pie_node_list = root.findall("./pies/pie")
for pie in pie_node_list:
  print(pie.text)

# use xpath syntax to find any cookie elements anywhere in tree
list_of_cookies = root.findall(".//cookie")
for cookie in list_of_cookies:
  print(cookie.text)


################################################################################################################
#  ATTRIBUTES - Access Attributes in combination with any other method to search and find an element
################################################################################################################
print("\nACCESS AND SEARCH ATTRIBUTE VALUES:")

tree = ET.parse("demo-xml.xml")
root = tree.getroot()

# use xpath syntax to find any cookie elements anywhere in tree
list_of_cookies = root.findall(".//cookie")
for cookie in list_of_cookies:
  print(cookie.text)
  print(cookie.get("sellby")) # print whatever is in the sellby attribute value for each element

# SEARCH BY ATTRIBUTE: notice how the inner value of the attribute in the search is inside single quotes
this_cookie = root.find(".//cookie[@sellby='03/15/2020']")
print("Cookie batch with sell by date of 03/15/2020: " + this_cookie.text)
