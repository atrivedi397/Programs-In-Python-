# Define a function and pass that list to sort
def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        minimum_index = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[minimum_index]:
                minimum_index = j
        unsorted_list[i], unsorted_list[minimum_index] = unsorted_list[minimum_index], unsorted_list[i]
    return unsorted_list


# Make an empty list and take input in them:
Size = int(input("\nHow many elements you want it to sort\n"))
to_be_sorted = []
for index in range(Size):
    try:
        to_be_sorted.append(int(input(f"\nProvide the value at index {index}\n>>> ")))
    except ValueError:
        pass

# Display sorted
print(f"Your sorted list is {selection_sort(to_be_sorted)}")
