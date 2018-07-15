# pass list to a function
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list


# Create and take input in a list
Size = int(input("\nHow many elements are there in the list ?\n"))
to_be_sorted = []
for index in range(Size):
    try:
        to_be_sorted.append(int(input(f"\nProvide a digit for input at index {index}\n>>> ")))
    except ValueError:
        pass

# display sorted
print(f"The sorted list is {bubble_sort(to_be_sorted)}")
