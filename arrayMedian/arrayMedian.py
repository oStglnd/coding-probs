

nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6]
#nums2 = [3, 4, 5, 6, 7]

def merge(a, b):
    # get length of arrays
    aLen = len(a)
    bLen = len(b)
    
    # new array f. sorted nums
    sortedArr = []
    
    # init indices
    aIdx = 0
    bIdx = 0
    
    # iteratively merge arrays
    while (aIdx < aLen) & (bIdx < bLen):
        
        if a[aIdx] < b[bIdx]:
            sortedArr.append(a[aIdx])
            aIdx += 1
        else:
            sortedArr.append(b[bIdx])
            bIdx += 1
    
    # return merged rests
    return sortedArr + a[aIdx:] + b[bIdx:]


def medianSortedArrays(nums1, nums2):    
    # get length of arrays
    n = len(nums1)
    m = len(nums2)
    
    # merge the two arrays
    mergedArr = merge(nums1, nums2)
    
    # find and return median
    mid = (n + m) // 2
    if (n + m) % 2 != 0:
        return mergedArr[mid]
    else:
        return (mergedArr[mid-1] + mergedArr[mid]) / 2
    
print(medianSortedArrays(nums1, nums2))