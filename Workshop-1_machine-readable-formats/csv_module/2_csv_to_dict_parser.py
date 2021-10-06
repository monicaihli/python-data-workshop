########################################################################################################################
# File: 2_csv_to_dict_parser.py
# Author: Monica Ihli
# Date: 9/22/2021

# Description: Uses csv module to map a CSV file that is read into a list of dictionaries.
# Documentation: https://docs.python.org/3/library/csv.html#csv.DictWriter

########################################################################################################################

import csv

print("\n\n***** EXAMPLE 1 *****\n\n")

with open('data_courses.csv', encoding='utf-8') as csvfile:
    my_dict_reader = csv.DictReader(csvfile)
    for row in my_dict_reader:
        print(row) # each line is returned as a dictionary


print("\n\n***** EXAMPLE 2 *****\n\n")

# the same thing but using some standard Python tools for manipulating diciontaries, such as iterating over
# key value pairs. Everything that works for a dictionary works here.
with open('data_courses.csv', encoding='utf-8') as csvfile:
    my_dict_reader = csv.DictReader(csvfile)
    for row in my_dict_reader:
        for key, value in row.items():
            print(key + ": " + value)
