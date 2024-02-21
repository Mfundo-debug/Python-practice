"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
 It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
 Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
 Example
 s = abc
This is a valid string because frequencies are {a: 1, b: 1, c: 1}.
s = abcc
This is a valid string because we can remove one c and have 1 of each character remaining in the string.
s = abccc
This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a: 1, b: 1, c: 2}.
Function Description

Complete the isValid function in the editor below.

isValid has the following parameter(s):

string s: a string
Returns

string: either YES or NO
Constraints
1 <= |s| <= 10^5
Each character s[i] is in ascii[a-z]
"""
def isValid(s):
    # create a dictionary to store the frequency of each character
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    # create a dictionary to store the frequency of each frequency
    freq_freq = {}
    for k, v in freq.items():
        if v in freq_freq:
            freq_freq[v] += 1
        else:
            freq_freq[v] = 1
    # if there is only one frequency, return YES
    if len(freq_freq) == 1:
        return "YES"
    # if there are two frequencies, and one of them is 1, return YES
    if len(freq_freq) == 2:
        keys = list(freq_freq.keys())
        if freq_freq[keys[0]] == 1 and (keys[0] - 1 == keys[1] or keys[0] == 1):
            return "YES"
        if freq_freq[keys[1]] == 1 and (keys[1] - 1 == keys[0] or keys[1] == 1):
            return "YES"
    return "NO"

if __name__ == '__main__':
    s =input()
    result = isValid(s)
    print(result)