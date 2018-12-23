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


def build_max_heap(Array, TotalElements):
    for k in range((TotalElements//2)-1, -1, -1):
        heapify(Array, TotalElements, k)


def heapsort(Array, TotalElements):
    build_max_heap(Array, TotalElements)
    for j in range(TotalElements - 1, -1, -1):
        Array[0], Array[j] = Array[j], Array[0]
        heapify(Array, j, 0)


array = []
Size = int(input("What is the size?\n"))

for i in range(Size):
    array.append(int(input("provide value")))

print(array)
heapsort(array, Size)

for i in range(0, Size):
    print(array[i])
