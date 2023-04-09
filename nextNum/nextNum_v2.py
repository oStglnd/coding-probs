
sampleNum1 = 5531
sampleNum2 = 112354
sampleNum3 = 155678
sampleNum4 = 12543

def nextNum(num: int) -> int:
    
    # make list of digits
    digitList = [int(s) for s in str(num)]
    n = len(digitList)
    
    # find the FIRST occurence of "decreasing" digits from RIGHT
    leftIdx = n-1
    for idx in range(1, n):
        if digitList[::-1][idx-1]> digitList[::-1][idx]:
            leftIdx = n - (idx+1)
            break
    
    # if not changed index, already max number
    if leftIdx == n-1:
        return num
    
    # find the LAST occurence of "decreasing" digits from LEFT
    rightIdx = 0
    for idx in range(1, n):
        if digitList[idx-1] >= digitList[idx]:
            rightIdx = idx

    # swap nums
    digitList[rightIdx], digitList[leftIdx] = digitList[leftIdx], digitList[rightIdx]
    
    # FLIP ta il IF idxs not adjacent
    digitList = digitList[:leftIdx+1] + digitList[leftIdx+1:][::-1]

    return int(''.join([str(i) for i in digitList]))