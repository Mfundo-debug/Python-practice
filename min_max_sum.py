"""
Given five positive integers, find the minimum and maximum values
 that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of 5 integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

Input Format

A single line of five space-separated integers.

Constraints
1 <= arr[i] <= 10^9
"""
import math 
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    arr.sort()
    for i in range(0, len(arr)-1):
        min_sum += arr[i]
    for j in range(1, len(arr)):
        max_sum += arr[j]
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)