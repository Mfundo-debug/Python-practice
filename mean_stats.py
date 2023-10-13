"""
Task

You are given a 2-D array of size NXM.
Your task is to find:

The mean along axis 1 
The var along axis 0 
The std along axis None
Input Format

The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.
"""
import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = np.array([input().split() for _ in range(N)], int)
    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    print(np.std(arr, axis=None))