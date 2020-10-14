#
#  Date:  Oct 13 2020
#  File:  case-1_B.py
#  Auth:  Monica Ihli monica@utk.edu


# in some situations, it will make more sense to separate out the downloading step from the parsing step

import requests # for making an http request
import xml.etree.ElementTree as ET  # for XML stuff
import glob, os # for our cool trick of finding all the files in a directory with a given file extension

baseurl = "http://volweb.utk.edu/~mihli1/demos/case1-C/"
files = ["file1.xml","file2.xml"]
headers = {"user-agent": "myemail@utk.edu"}

for f in files:
  url = baseurl + f # build the request URL for each file to be retrieved
  response = requests.get(url,headers) # notice that if you don't explicitly name parameters, they are implied by order
  if response.status_code == 200:
    with open(f, mode='wb') as localfile: # open a file of the same name and write it to disk (use correct mode!)qcu
      localfile.write(response.content) # fun trivia: response.text is string and response.content is raw bytes



# os.chdir("./") # you could offer another filepath to tell python to look somewhere else.
for f in glob.glob("*.xml"): # for every file in the current directory that ends in .xml
    print("\nNow parsing: " + f)
    tree = ET.parse(f)# we are using .parse() to load XML from a file stored on disk
    xml_data = tree.getroot() # extra step this way... get the root element from the tree

    # Display one element at a time
    for elem in xml_data:  # for every child node within root (cookies, pies)
      print(elem.tag, elem.text)  # print the element name. This first level of child nodes also has no text
