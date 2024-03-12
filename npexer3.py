"""
Create a numpy array, and find the recurrence of each element in the array and print the count of each element
after concatenate the arrays and pull from the concatenated array the unique elements and print the unique elements
"""
import numpy as np
def count_elements(arr):
    """
    Count the recurrence of each element in the array
    """
    return np.bincount(arr)

def unique_elements(arr1, arr2):
    """
    Concatenate the arrays and pull from the concatenated array the unique elements
    """
    return np.unique(np.concatenate((arr1, arr2)))

if __name__ == '__main__':
    arr1 = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
    arr2 = np.array([1, 0, 1, 0, 0, 1, 0, 1, 0, 0])
    print(count_elements(arr1))
    print(unique_elements(arr1, arr2))