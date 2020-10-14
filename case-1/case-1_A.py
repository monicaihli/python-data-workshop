#
#  Date:  Oct 13 2020
#  File:  case-1_A.py
#  Auth:  Monica Ihli monica@utk.edu


import requests # tell python you want to include functionality of this third party library


my_url = "http://volweb.utk.edu/~mihli1/demos/page1.html"
my_headers =  {'user-agent': 'myemail@utk.edu'} # user agent can just be some info to identify yourself to server
response_object = requests.get(url=my_url, headers=my_headers) # request what's at this address, just like if we were using a browser
if response_object.status_code == 200:
  print("Success")
  print("PAGE CONTENT:")
  print(response_object.content)  # print the contents of the page that we fetched


  # DEMONSTRATE DIFFERENT 3 WAYS TO GET TO THE SAME RESPONSE HEADERS
  print("\n*****  HEADERS  *****")
  resp_headers = response_object.headers  # assign the dictionary of values in the header to a variable
  print(resp_headers)  # dump the whole thing to console

  print("\n*****  HEADERS BY ITERATION *****")
  for item in resp_headers.items():  # .items() is one more trick for iterating over dictionaries.
    print("{}: {}".format(item[0], item[1]))  # each item of key-value pairs returned as tuple, so access by index

  print("\n*****  HEADERS BY KEY  *****")
  print("Date: " + resp_headers['Date'])
  print("Server: " + resp_headers['Server'])

else: # If you don't get a status code 200, something went wrong
  print("Status code " + str(response_object.status_code) + \
      ". Failed to fetch " + my_url) # convert status code from int to string and display it

print("\n\n")


# this other url intentionally goes nowhere, to demonstrate a problematic response code
my_other_url = "http://volweb.utk.edu/~mihli1/demos/bogus-url-goes-nowhere.html"
response_object2 = requests.get(my_other_url)
if response_object2.status_code == 200:
  print("Success")
else: # Will execute this code block because it failed to fetch the url
  print("Status code " + str(response_object2.status_code) + \
    ". Failed to fetch " + my_other_url)


