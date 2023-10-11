"""
Task

You are given a 2-D array with dimensions NXM.
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input Format

The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.
"""
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)
    print(np.prod(np.sum(arr, axis=0), axis=0))