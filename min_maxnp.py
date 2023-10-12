"""
Task

You are given a 2-D array with dimensions NXM.
Your task is to perform the min function over axis 1 and then find the max of that.

Input Format

The first line of input contains the space separated values of N and M
The next N lines contains M space separated integers.
"""
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)
    print(np.max(np.min(arr, axis=1), axis=0))