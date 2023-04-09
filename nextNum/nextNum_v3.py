

def nextNum(num: int) -> int:
    
    # make list of digits
    digitList = [int(s) for s in str(num)]
    n = len(digitList)
    
    leftIdx = n-1
    for i in range(1, n)[::-1]:
        if digitList[i] > digitList[i-1]:
            leftIdx = i-1
            break
    
    if leftIdx == n-1:
        return num
    
    rightIdx = leftIdx+1
    for i in range(rightIdx, n):
        if (digitList[i-1] > digitList[i]) & (digitList[i] > digitList[leftIdx]):
            rightIdx = i
    
    # SWAP
    digitList[leftIdx], digitList[rightIdx] = digitList[rightIdx], digitList[leftIdx]
    
    # FLIP
    if rightIdx - leftIdx > 1:
        digitList = digitList[:leftIdx+1] + digitList[leftIdx+1:][::-1]
    
    #return digitList
    return int(''.join([str(i) for i in digitList]))