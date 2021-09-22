########################################################################################################################
# File: xml_parser_3.py
# Author: Monica Ihli
# Date: 9/22/2021

# Description: Shows searching with a namespace and various methods of navigating a tree of XML elements.
# Documentation for ElementTree module: https://docs.python.org/3/library/xml.etree.elementtree.html
########################################################################################################################

import xml.etree.ElementTree as ET  # for XML stuff

tree = ET.parse("file3.xml") # load XML from a file stored on disk
xml_data = tree.getroot() # et the root element from the tree

print('*'*80 + '\n') # just gives us some visual space between tests

print("All children of root:\n\n")
for elem in xml_data:  # for every child node within root
    print(elem.tag, elem.text) # print tag name and text. NOTICE that some tags have a namespace!
    for subelem in elem:
        print(subelem.tag, subelem.text)
    print('\n')

########################################################################################################################
print('*'*80 + '\n') # just gives us some visual space between tests
########################################################################################################################

print("Element count with NO Namespace Qualifier:")
meal_plans = xml_data.findall("mealplan")
print(len(meal_plans))

print("Element count WITH Namespace:")
meal_plans = xml_data.findall("{some.food.URI.com}mealplan")
print(len(meal_plans))

print("An empty list is returned if we look for something and get no results:")
meal_plans = xml_data.findall("imaginary element")
print(len(meal_plans))

########################################################################################################################
print('*'*80 + '\n')
########################################################################################################################

print("Navigating Further Down the Tree - Mondays Only:")
meal_plans = xml_data.findall("{some.food.URI.com}mealplan")
for meal_plan in meal_plans:
    monday_dinner_element = meal_plan.find("meal[@day='Monday']") # search based on the attribute
    print(monday_dinner_element.text) # remember to use the .text attribute!
