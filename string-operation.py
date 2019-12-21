"""
Link to th question :
https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def merge_the_tools(string, k):
    # your code goes here
    """length = len(string)
    size_of_each = length//k
    m, n = 0, size_of_each
    list_of_word = []
    while n <= length:
        list_of_word.append(string[m:n])
        m = n
        n = n + size_of_each

    words_2 = []
    for word in list_of_word:
        new_word = ""
        for letter in word:
            if letter not in new_word:
                new_word += letter
        words_2.append(new_word)
    for item in words_2:
        print(item)
"""
    S, N = string, k
    for part in zip(*[iter(S)] * N):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
