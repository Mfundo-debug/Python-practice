"""
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. 
In an array, A, of size N, each memory location has some unique index, i (where 0 <= i <= N ), that can be referenced as A[i] or A_i.
Reverse an array of integers.

Example
A = [1,2,3]
Return [3,2,1] .

Function Description

Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):

int A[n]: the array to reverse
Returns
int[n]: the reversed array
Input Format

The first line contains an integer, N, the number of integers in A.
The second line contains N space-separated integers that make up A.

Constraints

1 <= N <= 10^3
1 <= A_i <= 10^4, where A_i is the i_th integer in A
"""
import math
import os
import random
import re
import sys

def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()