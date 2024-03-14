"""
Given an array, of [1,2,3,4,5], randomize the order of the elements in the array.
and use numpy to split the array into 2 arrays of equal length.
"""
def readarr(arr):
    import numpy as np
    np.random.shuffle(arr)
    print(arr)
    print(np.split(arr, 2))

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    readarr(arr)