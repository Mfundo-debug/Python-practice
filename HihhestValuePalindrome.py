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
    changes = [0]*n

    # Step 1: Make the string a palindrome
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            k -= 1
            changes[i] = 1
            s[i] = s[n-i-1] = max(s[i], s[n-i-1])

    if k < 0:
        return '-1'

    # Step 2: Maximize the palindrome
    i = 0
    while k > 0 and i < n//2:
        if s[i] < '9':
            if changes[i] == 1 and k >= 1:
                s[i] = s[n-i-1] = '9'
                k -= 1
            elif changes[i] == 0 and k >= 2:
                s[i] = s[n-i-1] = '9'
                k -= 2
        i += 1

    # If there's still changes left and the length is odd, maximize the middle digit
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