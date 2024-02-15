"""
Given two strings, determine if they share a common substring.
A substring may be as small as one character.
Example
s1 = 'and'
s2 = 'art'
These share the common substring a.
s1 = 'be'
s2 = 'cat'
These do not share a substring.
Function Description

Complete the function twoStrings in the editor below.

twoStrings has the following parameter(s):

string s1: a string
string s2: another string
Returns

string: either YES or NO
Constraints
s1 and s2 consist of characters in the range ascii[a-z].
1 <= |s1|, |s2| <= 10^5
1 <= p <= 10
"""
def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

if __name__ == "__main__":
    p = int(input().strip())
    for _ in range(p):
        s1 = input().strip()
        s2 = input().strip()
        print(twoStrings(s1, s2))