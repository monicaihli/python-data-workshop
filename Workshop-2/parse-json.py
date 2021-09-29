#
#  File:  parse_json.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates parsing JSON from string and from demo-json.json
#

import json

json_str = '{ "name":"Susan", "major":"Information Science", "gradyear":"2021"}'
print("The variable json_str is a {}".format(type(json_str)))  # print the type of the variable json_str

json_py_object = json.loads(json_str)  # use .loads() to read json from string

print(
  "The variable json_py_object is a {}".format(type(json_py_object)))  # print the type of the variable json_py_object

print("\n" + "*" * 80 + "\n")  # print a divider

with open("demo-json.json", "r") as read_file:
  data_list = json.load(read_file)  # use .load() to read the contents of the file into python data structures

  # set a break point on the print statement and use debug to take a better look at what's going on
for item in data_list['snacks']:
  print("The {} {} must be sold by {}.".format(item["type"], item["product"], item["sellby"]))
