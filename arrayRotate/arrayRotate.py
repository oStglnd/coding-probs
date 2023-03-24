

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4

def arrayRotate(arr, k):
    # assert that k is non-negative
    assert k >= 0
    
    # if k==0, return array w/o rotation
    if k == 0:
        return arr
    # else, slice and reorder
    else:
        return arr[-k:] + arr[:-k]