def binary_search(searching_list, element):
    begin = 0
    last = len(searching_list)-1
    if_found = False

    while begin <= last:
        mid = (begin + last)//2
        if element == searching_list[mid]:
            if_found = True
            break
        elif element > searching_list[mid]:
            begin = mid+1
        elif element < searching_list[mid]:
            last = mid-1
    print(f"found at {mid}") if if_found else print("not found")
