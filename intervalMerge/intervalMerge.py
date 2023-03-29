
inputList1 = [
    [1,3],[2,6],[8,10],[15,18]
]

inputList2 = [
    [1,4],[4,5]
]

inputList3 = [
    [1, 3], [4, 5], [6, 8], [2, 3], [8, 9]    
]

def overlapCheck(a: list, b: list) -> bool:
    
    if (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]):
        return True
    else:
        return False
    
def merge(a: list, b: list) -> list:
    
    return [min(a[0], b[0]), max(a[1], b[1])]

def intervalMerge(inputList: list) -> list:
    
    for aIdx, a in enumerate(inputList[:-1]):  
        bList = inputList[aIdx+1:]
        for bIdx, b in enumerate(bList):
            if overlapCheck(a, b):
                inputList[aIdx] = merge(a, b)
                del inputList[aIdx + bIdx + 1]
                
    return inputList