
nums = [2,7,11,15]
target = 9

def twoSum(nums: list, target: int) -> list:
    hashTab = {}    
    for idx, num in enumerate(nums):      
        if target - num in hashTab:
            return [hashTab[target-num], idx]
        else:
            hashTab[num] = idx