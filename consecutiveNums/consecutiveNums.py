
L = [5, 4, 2, 1]
K = [4, 7, 8, 1, 2, 0, -2]

def quickSort(unsortedList, idx=-1):
    pivot = unsortedList.pop(idx)
    leftList, rightList = [], []

    for elem in unsortedList:  
        if elem <= pivot:
            leftList.append(elem)
        else:
            rightList.append(elem)
            
    if len(leftList) > 1:
        leftList = quickSort(leftList)
        
    if len(rightList) > 1:
        rightList = quickSort(rightList)
        
    return leftList + [pivot] + rightList

def elemCount(a, b):
    return abs(b - a) - 1

def consecNums(L):
    L = quickSort(L)
    counter = 0
    for idx in range(len(L) - 1):
        counter += elemCount(L[idx], L[idx+1])
        
    return counter
    
    