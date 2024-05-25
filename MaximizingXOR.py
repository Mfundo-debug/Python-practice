"""
Given two integers, l and r, find the maximal value of a xor b, where a and b satisfy the following condition:'
l <= a <= b <= r
for example, if l=11 and r=12, then
11 xor 11 = 0
11 xor 12 = 7
12 xor 12 = 0
The maximum value is 7.

Function Description

Complete the maximizingXor function in the editor below. It must return an integer representing the maximum value calculated.

maximizingXor has the following parameter(s):

l: an integer, the lower bound, inclusive
r: an integer, the upper bound, inclusive

Constraints
1 <= l <= r <= 10^3
"""

def maximizingXor(l, r):
    max_xor = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            xor = i ^ j
            if xor > max_xor:
                max_xor = xor
    return max_xor

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maximizingXor(l, r))