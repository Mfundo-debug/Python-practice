"""
Task

You are given two integer arrays, A and B of dimensions NXM.
Your task is to perform the following operations:

Add ( A+B )
Subtract ( A-B)
Multiply (A*B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)
Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format

The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.
"""

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = np.array([input().split() for _ in range(n)], int)
    b = np.array([input().split() for _ in range(n)], int)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)