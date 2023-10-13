"""
Task

You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.

Input Format
import numpy as np

if __name__ == '__main__':
    A, B = (np.array([input().split() for _ in range(int(input()))], int) for _ in range(2))
    print(np.dot(A, B))
The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array A.
"""
import numpy as np

if __name__ == '__main__':
    N = int(input())
    A = np.array([input().split() for _ in range(N)], int)
    B = np.array([input().split() for _ in range(N)], int)
    print(np.dot(A, B))
    