#! /usr/local/bin/python3.6

# take files from the command line:
# a user can give as many files to read from
# and a redirection (in case wants to append the output to the last file in command line)
import sys
command, *files_and_symbols = sys.argv


# read files one by one and return a string having contents
def read_given_files(*files):
    file_objects = []
    for file in files:
        f_obj = open(file, 'r')
        f_obj_read = f_obj.read()
        file_objects.append(f_obj_read)
    return "".join(file_objects)


# If there is command for redirection then
# output of all the files is appended to the last file
if (">>" or "1>>" or ">>") in files_and_symbols:
    passed_files = files_and_symbols[:-2]
    w_file_object = open(files_and_symbols[-1], "r+")
    w_file_object.write(read_given_files(*passed_files))
    w_file_object.close()

# Else printed to screen
else:
    print(read_given_files(*files_and_symbols))
