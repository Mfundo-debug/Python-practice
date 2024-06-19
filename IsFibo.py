"""
You are given an integer, N. Write a program to determine if N is an element of the Fibonacci sequence.
The first few elements of the Fibonacci sequence are 0,1,1,2,3,5,8,13....
A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. 
The first two elements are 0 and 1.
Function Description

Complete the isFibo function in the editor below.

isFibo has the following parameters:
- int n: the number to check

Returns
- string: either IsFibo or IsNotFibo

Constraints
1 ≤ t ≤ 10^5
1 ≤ n ≤ 10^10
"""
def isFibo(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if a == n:
        return "IsFibo"
    else:
        return "IsNotFibo"
    
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        print(isFibo(n))