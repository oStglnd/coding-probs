
input1 = 19
input2 = 110
input3 = 256
input4 = 797

def primeTimeSimple(inputInt: int) -> bool:
    
    if inputInt == 0 or inputInt == 1:
        return True
    else:
        for i in range(2, inputInt):
            if inputInt % i == 0:
                return False
    
    return True
    