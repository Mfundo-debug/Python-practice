"""
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome.
There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
Example
s = 'bcbc'
Either remove 'b' at index 0 or 'c' at index 3.
Function Description

Complete the palindromeIndex function in the editor below.

palindromeIndex has the following parameter(s):

string s: a string to analyze
Returns

int: the index of the character to remove or -1
Constraints
1 <= q <= 20
1 <= |s| <= 10^5 + 5
All characters are in the range ascii[a-z].
"""
def palindromeIndex(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            if s[i] == s[-(i + 2)] and s[i + 1] == s[-(i + 3)]:
                return len(s) - i - 1
            else:
                return i
    return -1

if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(palindromeIndex(s))