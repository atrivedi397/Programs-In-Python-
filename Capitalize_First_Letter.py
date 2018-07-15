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

'''
# Capitalize the First Letter of the word (Make a function
# for this which takes an word argument and capitalize the first letter)
def make_first_letter_capital(word):
    if not word[0].isupper():
        return word.replace(word[0], word[0].upper())


# Clearing the file contents  to write the new ones



for Word in f_obj_str:
    if '\n' in Word:

        if Word.endswith('\n'):
            Word = make_first_letter_capital(Word.strip('\n'))
            f_obj.write(Word + '\n')

        elif Word.startswith('\n'):
            Word = make_first_letter_capital(Word.strip('\n'))
            f_obj.write('\n' + Word)

        else:
            word1, word2 = tuple(Word.split('\n'))
            word1 = make_first_letter_capital(word1.strip('\n')) + ' '
            word2 = make_first_letter_capital(word2.strip('\n')) + ' '
            f_obj.write(word1 + "\n" + word2)

    else:
        Word = make_first_letter_capital(Word) + " "
        f_obj.write(Word)


f_obj.close()
'''"""
This Is The Script For Capitalizing The First Letter Of Each Of The
Word In A Given File Of String. This Script Takes A String File As An Argument.
"""
