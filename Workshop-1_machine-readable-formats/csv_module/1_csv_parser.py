########################################################################################################################
# File: 1_csv_parser.py
# Author: Monica Ihli
# Date: 9/22/2021

# Description: Demonstrates simple implementation of parsing a CSV file.
# Documentation for csv module: https://docs.python.org/3/library/csv.html
########################################################################################################################
import csv

print("\n***** EXAMPLE 1 *****\n")
# Most simple example of reading output one line at a time
with open('data_courses.csv', encoding='utf-8') as csvfile:
     my_csv_reader = csv.reader(csvfile)
     for row in my_csv_reader:
         print(my_csv_reader.line_num) # remember that line number property is going to increment with each pass
         print(row)  # each row object is a list. Each list contains one string for every column.


print("\n\n***** EXAMPLE 2 *****\n\n")

# Each row of data is read into a Python list. So we can use all our standard Python list tools
# to manipulate and interact with the data. This is the objective of our workflow: Get the RAW data into
# something that Python can use!

with open('data_courses.csv', encoding='utf-8') as csvfile:
    my_csv_reader = csv.reader(csvfile)
    next(my_csv_reader) # we are forcing to increment by 1 to skip the header row
    total_credits = 0 # setup a placeholder for adding stuff
    for row in my_csv_reader:
         print(row[0] + ": " + row[1] + " - " + row[2]) # print each course info
         total_credits += int(row[3])


    print("These courses add up to " + str(total_credits) + " credit hours.")

