"""
Consider two non-negative long integers, a and b, where a <= b. We define the bitwise AND of all natural numbers in the inclusive range [a, b] as follows:
the inclusive range between a and b is [a, a+1, a+2, ..., b-1, b] where '&' represents the bitwise AND operation.
Given n pairs of long integers, a[i] and b[i], compute and print the bitwise AND of all natural numbers in the inclusive range between a[i] and b[i].
For example, if a = 10 and b = 14, the bitwise AND of the inclusive range [10, 11, 12, 13, 14] is 8.
Function Description

Complete the andProduct in the editor below. It should return the computed value as an integer.

andProduct has the following parameter(s):

a: an integer
b: an integer

Constraints
1 <= n <= 200
0 <= a <= b <= 2^32
"""

def andProduct(a, b):
    if a == b:
        return a
    else:
        return a & b & ((a ^ b).bit_length() - 1)
    
if __name__ == '__main__':
    n = int(input().strip())
    for n_itr in range(n):
        ab = input().rstrip().split()
        a = int(ab[0])
        b = int(ab[1])
        result = andProduct(a, b)
        print(result)