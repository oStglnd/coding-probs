
sampleDigit1 = 5531
sampleDigit2 = 112354
sampleDigit3 = 155678

def nextDigit(digit: int) -> int:
        
    # turn digit into list
    digitList = [int(s) for s in str(digit)]
    n = len(digitList)
    
    # find the first occurence of "decreasing" digits from left
    leftIdx = n - 1
    for idx in range(1, n):
        if digitList[::-1][idx] < digitList[::-1][idx-1]:
            leftIdx = n - (idx+1)
            break
    
    # if not changed index, already max number
    if leftIdx == n - 1:
        return digit
    
    # find the first occurence of "decreasing" digits from right
    rightIdx = -1
    for idx in range(1, n):
        if digitList[idx] < digitList[idx-1]:
            rightIdx = idx
            break
        
    digitList[leftIdx], digitList[rightIdx] = digitList[rightIdx], digitList[leftIdx]
    return int(''.join([str(num) for num in digitList]))