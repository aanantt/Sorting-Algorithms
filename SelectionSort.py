def selectionSort(array):
    for i in range(len(array)):
        minindex = i
        for j in range(i+1, len(array)):
            if array[j] < array[minindex]:
                minindex = j
        if i!=minindex:
           array[i], array[minindex] = array[minindex], array[i]
    return array
print(selectionSort([1,5,8,2,9,0]))