"""
Given an array of integers, where all elements but one occur twice, find the unique element.
Example
a = [1, 2, 3, 4, 3, 2, 1]
the unique element is 4
Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
Input Format

The first line contains a single integer, n, the number of integers in the array.
The second line contains n space-separated integers that describe the values in a.

Constraints
1 <= n < 100
It is guaranteed that n is an odd number and that there is one unique element.
0 <= a[i] <= 100, where 0 <= i < n
"""
def lonelyinteger(a):
    # Write your code here
    result = 0
    for i in a:
        result ^= i
    return result
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(lonelyinteger(a))