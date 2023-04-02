
sampleString1 = 'aaaaAAbbCddddEEE'
sampleString2 = 'gggHHjkkPPlmNNooooo'


def stringRLE(regString: str) -> str:
        
    # get first character and init counter
    char = regString[0]
    count = 1
    
    # iteratively add elements to encoded string
    encodedStr=''
    for idx, nextChar in enumerate(regString[1:]):
        
        if nextChar == char:
            count += 1
        else:
            encodedStr += str(count) + char
            char = nextChar
            count = 1
    
    # add last char/elem nto encoded string
    encodedStr += str(count) + char
    
    return encodedStr