def bubbleSort(array):
    for i in range(0,len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
print(bubbleSort([1,5,8,2,9,0]))