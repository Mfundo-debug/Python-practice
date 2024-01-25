"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
Example
s = 'The quick brown fox jumps over the lazy dog'
The string contains all letters in the English alphabet, so return pangram.
Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

string s: a string to test
Returns

string: either pangram or not pangram
Constraints
0 <= |s| <= 10^3
Each character of s, s[i] E {a-z, A-Z, space}
"""
def pangrams(s):
    s = s.lower()
    s = s.replace(" ", "")
    s = set(s)
    if len(s) == 26:
        return "pangram"
    else:
        return "not pangram"
    
if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)