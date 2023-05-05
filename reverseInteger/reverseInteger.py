
i = 123

def reverseInteger(x: int) -> int:
    # check edge case
    if x == 0:
        return 0
    else:
        # convert to string
        xString = str(x)
        
        # if negative, account for first char
        if x < 0:
            return -int(xString[1:][::-1])
        # if positive, reverse and return as int
        else:
            return int(xString[::-1])