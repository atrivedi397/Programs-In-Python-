def print_formatted(number):
    # your code goes here
    number_bin = str(bin(number))
    length = len(number_bin)
    for i in range(1, number + 1):
        print(i, length*' ', str(oct(i)).lstrip('0o'), length*' ', str(hex(i)).lstrip('0x').upper(), length*' ', str(bin(i)).lstrip('0b'))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
