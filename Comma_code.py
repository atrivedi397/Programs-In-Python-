import copy


def comma_code(argument):
    argument = copy.copy(argument)
    argument.insert(-1, 'and')
    string = str()
    for i in range(len(argument)):
        if i < len(argument)-1:
            string += argument[i]
            string += ', '
        if i == len(argument)-1:
            string += argument[i]
    print(f'\'{string}\'')


topper = ['hello', 'its', 'me', 'thanks', 'its dark here']


comma_code(topper)
print(topper)
