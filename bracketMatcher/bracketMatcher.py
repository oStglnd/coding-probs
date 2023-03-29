

inputStr = "(coder)(byte))"

def bracketMatch(inputStr: str) -> bool:
    
    counter = 0
    
    for s in inputStr:
        
        if s=='(':
            counter += 1
        elif s==')':
            counter -= 1
        else: 
            continue
        
        if counter < 0:
            return False
        
    return counter == 0