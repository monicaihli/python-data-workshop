########################################################################################################################
# File: xml_parser_1.py
# Author: Monica Ihli
# Date: 9/22/2021

# Description: Emphasizes reading XML data from files using the .parse() method from xml.etree.ElementTree
#              Looks for all XML files in the current directory and loads to an XML tree. Prints immediate children
#              of the root element for each file.
# Documentation for ElementTree module: https://docs.python.org/3/library/xml.etree.elementtree.html
########################################################################################################################

import xml.etree.ElementTree as ET  # for XML stuff
import glob # for our cool trick of finding all the files in a directory with a given file extension

for f in glob.glob("*.xml"): # for every file in the current directory that ends in .xml
    print("\nNow parsing: " + f)
    tree = ET.parse(f) # we are using .parse() to load XML from a file stored on disk
    xml_data = tree.getroot() # extra step not found with fromstring() - get the root element from the tree

    # Display one element at a time
    for elem in xml_data:  # for every child node within root (cookies, pies)
      print(elem.tag, elem.text)  # print the element name. This first level of child nodes also has no text