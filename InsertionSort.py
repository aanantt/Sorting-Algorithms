def insertionSort(array):
    for i in range(len(array)):
        j=i-1
        while array[j] > array[j+1] and j >=0:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array
print(insertionSort([1,5,8,2,9,0]))