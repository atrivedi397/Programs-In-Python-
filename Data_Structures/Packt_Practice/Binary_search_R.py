"""
    # Alternative Way:

    def binary_search(any_list, element):
        if len(any_list) > 0:
            mid = len(any_list)//2
            if element == any_list[mid]:
                return True
            elif element < any_list[mid]:
                return binary_search(any_list[:mid], element)
            elif element > any_list[mid]:
                return binary_search(any_list[mid+1:], element)
        else:
            return False
"""


def binary_search_re(any_list, element, beg, last):
    mid = (beg + last)//2
    if beg <= last:
        if element == any_list[mid]:
            print(f"found at {mid}")
            return
        elif element < any_list[mid]:
            binary_search_re(any_list, element, beg, mid-1)
        elif element > any_list[mid]:
            binary_search_re(any_list, element, mid+1, last)
    else:
        print("Not Found")
