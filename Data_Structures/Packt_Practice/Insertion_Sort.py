# Creating function for Insertion Sort
def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        key_element = unsorted_list[i]
        j = i-1
        while j >= 0 and unsorted_list[j] > key_element:
            unsorted_list[j+1] = unsorted_list[j]
            j = j-1
        unsorted_list[j+1] = key_element
    return unsorted_list


# Taking inputs in a list
Size = int(input("\nWhat is the size of list of elements ?\n"))
to_be_sorted = []
for index in range(Size):
    try:
        to_be_sorted.append(int(input(f"\nProvide the number for index {index}\n>>> ")))
    except ValueError:
        pass

# Display the sorted list
print(f"The sorted list is {insertion_sort(to_be_sorted)}")
