# Collatz function takes an argument and returns floor division if number is even otherwise 3*number +1.
# It is a sequence which finally arrives at 1 sooner or later, works for any integer.
# Its values are added in a list till the output or sequence is not 1


def collatz(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    except ValueError:
        print("You just have to enter a number")


answer_list = [0]
while answer_list[0] != 1:
    digit = input('Input your number: \n')
    answer_list.insert(0, collatz(digit))
    print(answer_list)
