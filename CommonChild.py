"""
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. 
Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

Example
s1 = 'ABCD'
s2 = 'ABDC'
These strings have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Return 3.
Function Description

Complete the commonChild function in the editor below.

commonChild has the following parameter(s):

string s1: a string
string s2: another string
Returns

int: the length of the longest string which is a common child of the input strings

Constraints
1 <= |s1|, |s2| <= 5000 where |s| is the length of string s.
All characters are upper case in the range ascii[A-Z].
"""
def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(result)