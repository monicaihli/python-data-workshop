########################################################################################################################
# File: 3_dict_writer.py
# Author: Monica Ihli
# Date: 9/22/2021

# Description: Uses csv module create an object which maps dictionaries onto output rows.
# Documentation: https://docs.python.org/3/library/csv.html#csv.DictWriter

########################################################################################################################

import csv

with open('dictwriter_output.csv', mode='w', encoding='utf-8') as output_file:
    fieldnames = ['first_name', 'last_name', 'grade']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames) # pass file handler and fieldnames as arguments

    writer.writeheader() # write the header row (column labels) to file

    # the writerow() method is called and passed a dictionary for each row of data it should create
    writer.writerow({'first_name': 'Twilight', 'last_name': 'Sparkles', 'grade' : 'A++'}) #
    writer.writerow({'first_name': 'Puss', 'last_name': 'In Boots', 'grade': 'B'})
    # in the form of a dictionary saved to a variable first:
    example_dictionary = {'first_name': 'Geralt', 'last_name': 'of Rivia', 'grade': 'A'}
    writer.writerow(example_dictionary)