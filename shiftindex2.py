"""

Shift index level2: given the arrray and the shift value, the function will shift the index of the array by the shift value.

"""


import numpy as np

def shift_index_level2(arr, shift):
    # Create a new array with the same shape as the input array
    new_arr = np.empty_like(arr)
    
    # Calculate the new indices
    new_indices = (np.arange(arr.shape[0]) + shift) % arr.shape[0]
    
    # Assign the values from the original array to the new array
    for i in range(arr.shape[0]):
        new_arr[i] = arr[new_indices[i]]
    
    return new_arr