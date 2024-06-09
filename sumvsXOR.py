"""
Given an integer n, find each x such that:
0 <= x <= n
n + x = n ^ x
where ^ denotes the bitwise XOR operator. Print the number of x's satisfying the criteria.
Example
n = 4
There are four values that satisfy the condition:
4 + 0 = 4 ^ 0 = 4
4 + 1 = 4 ^ 1 = 5
4 + 2 = 4 ^ 2 = 6
4 + 3 = 4 ^ 3 = 7
Return 4.
Function Description

Complete the sumXor function in the editor below.

sumXor has the following parameter(s):
- int n: an integer

Returns
- int: the number of values found
Input Format
A single integer, n.
Constraints
0 <= n <= 10^5
Subtasks
0 <= n <= 100 for 60% of the maximum score.
"""
def sumXor(n):
    count = 0
    while n:
        count += n % 2 == 0
        n //= 2
    return 2 ** count
if __name__ == '__main__':
    n = int(input())
    result = sumXor(n)
    print(result)