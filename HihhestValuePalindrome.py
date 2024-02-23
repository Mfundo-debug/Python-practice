"""
Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make.
 Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. 
 The length of the string may not be altered, so you must consider 0's left of all higher digits in your tests. For example 0110 is valid, 0011 is not.
Given a string representing the starting number, and a maximum number of changes allowed, 
create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints. 

Example
s = '1231'
k = 3
Make 3 replacements to get '9339'.
s = '12321'
k=1
make 1 replacement to get '12921'.
Function Description

Complete the highestValuePalindrome function in the editor below.

highestValuePalindrome has the following parameter(s):

string s: a string representation of an integer
int n: the length of the integer string
int k: the maximum number of changes allowed
Returns

string: a string representation of the highest value achievable or -1
Constraints
0 <= n <= 10^5
0 <= k <= 10^5
Each character i in the number is an integer where 0 <= i <= 9
"""
def highestValuePalindrome(s, n, k):
    s = list(s)
    diff = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            diff += 1
    if diff > k:
        return '-1'
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            if s[i] > s[n-i-1]:
                s[n-i-1] = s[i]
            else:
                s[i] = s[n-i-1]
                k -= 1
    for i in range(n//2):
        if s[i] != '9':
            if k >= 2 and s[i] == s[n-i-1]:
                s[i] = s[n-i-1] = '9'
                k -= 2
            elif k >= 1 and s[i] != s[n-i-1]:
                s[i] = s[n-i-1] = '9'
                k -= 1
    if k > 0 and n%2 == 1:
        s[n//2] = '9'
    return ''.join(s)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()
    result = highestValuePalindrome(s, n, k)
    print(result)