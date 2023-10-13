"""
Task

You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array A.
The second line contains the space separated elements of array B.
"""
import numpy as np

if __name__ == '__main__':
    A = np.array(input().split(), int)
    B = np.array(input().split(), int)
    print(np.inner(A, B))
    print(np.outer(A, B))