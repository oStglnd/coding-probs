
input1 = 19
input2 = 110
input3 = 256
input4 = 797

def primeTime(inputInt: int) -> bool:
    
    if inputInt == 0 or inputInt == 1:
        return True
    
    primeBools = [True] * (inputInt)
    maxInt = int(inputInt ** .5) + 1
    for i in range(2, maxInt):
        if primeBools[i]:
            n = i**2  
            while n < inputInt:
                primeBools[n] = False
                n += i
    
    primeNums = [idx for idx, ind in enumerate(primeBools) if ind]
    for prime in primeNums[2:]:
        if inputInt % prime == 0:
            return False
    
    return True
    