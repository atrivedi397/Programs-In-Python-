#! usr/local/bin/python3.6

# sys for command line arguments and re for regular exprssions
import re
import sys

script, file_to_read = sys.argv
print(f"This {script} is used to check patterns of a number in a file")


number_search_pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d')


# passing raw strings -> r'' so that escape characters not escaped
# \d -> means match any digit (0-9)
def number_match(aline):
    match_object = number_search_pattern.search(aline)
    print("Number found :" + match_object.group())
    print(f"Alternatively : Number found : {number_search_pattern.findall(file_str)}")


file_obj = open(file_to_read)
file_str = file_obj.read()
number_match(file_str)
