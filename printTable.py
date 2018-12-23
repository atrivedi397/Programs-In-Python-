tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(argument):

    # creating a list of size 3 wherein indicies will
    # store the maximum of the length of the all strings in a given list
    col_width = [0] * len(argument)

    # creating nested empty list to store the lengths
    # of the strings in the given nested list argument
    max_length = [[] for _ in range(len(argument))]

    # taking inputs for the max_length list which are storing the
    # lengths of the strings of their respective indicies as in the given argument
    for i in range(len(argument)):
        for j in range(len(argument[i])):
            max_length[i].append(len(argument[i][j]))

        # sorting in place which will make easy to get maximum size
        max_length[i].sort(reverse=True)

    print(max_length)

    for i in range(len(max_length)):
        col_width[i] = max(max_length[i])
    print(col_width)

    for i in range(4):
        for j in range(3):
            print(argument[j][i].rjust(col_width[j]), end='  ')
        print()


print_table(tableData)
