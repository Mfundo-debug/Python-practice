"""
Task

You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions, 
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Constraints
1 <= each integer <= 3
"""

import numpy as np

if __name__ == '__main__':
    nums = tuple(map(int, input().split()))
    print(np.zeros(nums, dtype=np.int))
    print(np.ones(nums, dtype=np.int))