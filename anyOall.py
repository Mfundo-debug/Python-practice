"""
Task

You are given a space separated list of integers. If all the integers are positive, 
then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N  integers.

Constraints
0 < N < 100
"""
def is_palindrome(n):
    return str(n) == str(n)[::-1]
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(all([i>0 for i in arr]) and any([is_palindrome(i) for i in arr]))