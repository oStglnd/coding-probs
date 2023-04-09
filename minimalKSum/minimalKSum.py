
nums = [1,4,25,10,25]
k = 2

def spaceCheck(a: int, b: int) -> int:
    assert a <= b
    
    if a == b:
        return 0
    else:    
        return (b - a) - 1


def minimalKSum(nums: list, k: int) -> int:
    
    # sort nums
    nums.sort()
    
    # if k is 0, no list needed
    if k == 0:
        return 0
    elif k < nums[0]:
        return sum(range(1, k+1))
    else:
        intSum = 0
        for i in range(1, nums[-1]):
            if i in nums:
                del nums[0]
            else:
                intSum += i
                k -= 1
                if k == 0:
                    return intSum
     
    return intSum + sum(range(nums[-1], nums[-1] + k + 1))
        
        