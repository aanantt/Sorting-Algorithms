def quickSort(a_list):
    if len(a_list) < 2: return a_list
    lesser = quickSort([x for x in a_list[1:] if x <= a_list[0]])
    bigger = quickSort([x for x in a_list[1:] if x > a_list[0]])
    return lesser+[a_list[0]]+bigger
print(quickSort([1,5,3,8,9,2]))