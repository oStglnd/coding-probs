
input1 = ["ahffaksfajeeubsne", "jefaa"]
input2 = ["aaffhkksemckelloe", "fhea"]

def windowChecker(window: str, b: str) -> bool:
    
    windowList = list(window)
    for s in b:
        if s in windowList:
            del windowList[windowList.index(s)]
        else:
            return False
    
    return True
    

def minWinStr(arr: list) -> str:
    A = arr[0]
    B = arr[1]
    
    nA = len(A)
    nB = len(B)
    
    for windowSize in range(nB, nA):
        windows = [A[i:i+windowSize] for i in range(nA - windowSize)]
        for window in windows:
            if windowChecker(window, B):
                return window
        
    return A