"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
Example
s = 'abcac'
n = 10
The substring we consider is abcacabcac, the first 10 characters of the infinite string.
Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Constraints
1 <= |s| <= 100
1 <= n <= 10^12
For 25% of the test cases, n <= 10^6.
"""
def repeatedString(s,n):
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    count = count * (n//len(s))
    for i in range(n%len(s)):
        if s[i] == 'a':
            count += 1
    return count
if __name__ == '__main__':
    s = input()
    n = int(input())
    print(repeatedString(s,n))