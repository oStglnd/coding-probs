
lists = [[1,4,5],[1,3,4],[2,6]]

def mergeKLists(lists: list) -> list:
    newList = []    
    listIdx = 0

    while len(lists) > 1:
        minVal = 1e16
        for idx, intList in enumerate(lists):

            if (intList[0] < minVal):
                listIdx = idx
                minVal = intList[0]
            
        val = lists[listIdx].pop(0)
        newList.append(val)
        
        if len(lists[listIdx]) == 0:
            del lists[listIdx]
    
    newList += lists[0]
    
    return newList
