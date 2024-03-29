"""
Task

You are given a square matrix A with dimensions NXN. 
Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer N.
The next N lines contains the N space separated elements of array A.
"""
import numpy

if __name__ =='__main__':
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], float)
    print(round(numpy.linalg.det(a),2))