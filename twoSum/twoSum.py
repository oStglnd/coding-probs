
nums = [2,7,11,15]
target = 9

def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i, len(nums)):        
            if nums[i] + nums[j] == target:
                return [i, j]