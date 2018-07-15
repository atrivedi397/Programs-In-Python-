# This is a script to count the number of occurences of a character in a file given
# as an argument.

import sys, pprint
script, filename = sys.argv


def count_chars(file_object):
    count = {}
    for character in file_object:
        count.setdefault(character, 0)
        count[character] = count[character]+1
    return count


file_object = open(filename, encoding='utf-8')
file_object = file_object.read()
pprint.pprint(count_chars(file_object))
