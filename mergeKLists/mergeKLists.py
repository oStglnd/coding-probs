
lists = [[1,4,5],[1,3,4],[2,6]]

def mergeKLists(lists: list) -> list:
    newList = []    
    listIdx = 0
    
    while sum([len(intList) > 0 for intList in lists]) > 1:
        minVal = 1e16
        for idx, intList in enumerate(lists):
            try:
                if (intList[0] < minVal):
                    listIdx = idx
                    minVal = intList[0]
            except IndexError:
                continue
            
        val = lists[listIdx].pop(0)
        newList.append(val)
    
    for intList in lists:
        newList += intList
    
    return newList
