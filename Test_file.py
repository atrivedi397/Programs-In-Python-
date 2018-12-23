# STEP 1 "finding the maximum"
def max(arr):
    global largest
    largest = arr[0]
    for i in range(1, size):
        if largest < arr[i]:
            largest = arr[i]

    print("\n largest is", largest)


def count_sort():
    b = []
    c = []
    # STEP 2initializing the elements of new array as 0
    for i in range(0, largest + 1):
        b.append(0)

    # STEP -3 finding the frequency of each number and placing it in new array
    for i in range(0, largest + 1):
        c = 0
        for j in range(0, size):
            if i == arr[j]:
                c += 1
        print("the frequency of", i, "is", c)

        b[i] = c
    print("now the b array contains")
    for i in range(0, largest + 1):
        print(b[i], end="  ")

    # step 4 find the commulative frequency
    for i in range(1, largest + 1):
        b[i] = b[i] + b[i - 1]
    print("\n now the b array contains")
    for i in range(0, largest + 1):
        print(b[i], end="  ")

    # STEP S SORTING

    for i in range(0, size):
        c[b[arr[i]] - 1] = arr[i]
        b[arr[i]] = b[arr[i]] - 1
    print("\nthe sorted array is ")
    for i in range(0, size):
        print(c, end="  ")


arr = []

size = int(input("ENTER THE SIZE OF THE ARRAY"))
for i in range(0, size):
    arr.append(int(input("enter the elements")))

print("the values entered by the user are :")
for i in range(0, size):
    print(arr[i], end=" ")

largest = 0
max(arr)
count_sort()
