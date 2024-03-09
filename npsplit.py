"""
Splitting arrays using numpy
"""
def split_array(arr, axis=0):
    """
    Split an array into sub-arrays
    """
    if axis == 0:
        return arr[:len(arr)//2], arr[len(arr)//2:]
    elif axis == 1:
        return arr[:, :arr.shape[1]//2], arr[:, arr.shape[1]//2:]
    else:
        return None
    
if __name__ == '__main__':
    import numpy as np
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(split_array(arr, axis=0))
    print(split_array(arr, axis=1))
    print(split_array(arr, axis=2))