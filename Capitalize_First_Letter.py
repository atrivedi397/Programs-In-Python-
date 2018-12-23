"""
This is the script for capitalizing the first Letter of each of the
word in a given file of string. This script takes a string file as an argument.
"""
# !~/anaconda3/bin/python3.6

# Read a Text file or a line from a text file
from sys import argv
import string
script, file_name = argv

# Creating a file object to perform reading and writing
f_obj = open(file_name, 'r+')

# reading line by line and appending it to a list
to_write = []
for line in f_obj:
    to_write.append(line)

# capitalizing first letter of each word of the line
for index in range(len(to_write)):
    to_write[index] = string.capwords(to_write[index])

f_obj.write('\n'.join(to_write))
f_obj.close()
