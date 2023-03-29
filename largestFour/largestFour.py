
inputList1 = [1, 5, 4, 2, 6, 8, 6, 5, 3, 4, 6, 8, 11]
inputList2 = [5, 4, 1, 22, 3, 11, 5, 77, 5, 4, 44, 3, 123, 53, 2]

def bubbleSort(unsortedList: list) -> list:
    
    listSorted = True
    for idx in range(len(unsortedList) - 1):    
        if unsortedList[idx] > unsortedList[idx+1]:
            temp = unsortedList[idx]
            unsortedList[idx] = unsortedList[idx+1]
            unsortedList[idx+1] = temp
            listSorted = False

    if listSorted:
        return unsortedList
    else:
        return bubbleSort(unsortedList)


def fourFinder(inputList: list) -> int:
    
    if len(inputList) == 0:
        return 0
    
    elif len(inputList) <= 4:
        return sum(inputList)
    
    else:
        bubbleSort(inputList)
        return sum(inputList[-4:])
    
    
print(fourFinder(inputList1))
print(fourFinder(inputList2))