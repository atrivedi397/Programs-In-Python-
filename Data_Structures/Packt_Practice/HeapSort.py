from math import floor


def heapify(Array, ElementsInHeap, Index):
    largest = Index
    leftChild = Index*2 + 1
    rightChild = Index*2 + 2

    if leftChild < ElementsInHeap and Array[largest] < Array[leftChild]:
        largest = leftChild

    if rightChild < ElementsInHeap and Array[largest] < Array[rightChild]:
        largest = rightChild

    if largest != Index:
        Array[Index], Array[largest] = Array[largest], Array[Index]
        heapify(Array, ElementsInHeap, largest)


def build_max_heap(Array):
    TotalElements = len(Array)
    for k in range(floor(TotalElements/2), -1, -1):
        heapify(Array, TotalElements, k)


def heapsort(Array, TotalElements):
    build_max_heap(Array)
    for j in range(TotalElements - 1, 0, -1):
        Array[0], Array[j] = Array[j], Array[0]
        heapify(Array, j, 0)
        print("After every swap the array is\n", array)


array = []
Size = int(input("What is the size?\n"))

for i in range(0, Size):
    array.append(input("provide value"))

heapsort(array, len(array))

for i in range(0, Size):
    print(array[i], "\n")
