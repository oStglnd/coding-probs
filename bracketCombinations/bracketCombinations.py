
import math

inputNum = 3
inputNum = 7

def catalanNum(n):
    if (n == 0) | (n == 1):
        return 1
    
    else:
        catNum = 1
        for k in range(2, n+1):
            catNum *= (n + k) / k
            
        return math.ceil(catNum)
    
def bracketCombinations(n):
    
    return catalanNum(n)