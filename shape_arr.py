"""
Task

You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format

A single line of input containing  space separated integers.

Output Format

Print the 3X3 NumPy array.
"""
import numpy as np

def shape_arr():
    arr = np.array(input().split(), int)
    arr.shape = (3, 3)
    print(arr)

if __name__ == '__main__':
    shape_arr()