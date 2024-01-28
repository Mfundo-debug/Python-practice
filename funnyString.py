"""
In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g.abc -> cba . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny
Example
s = 'lmnop'
The ordinal values of the charcters are [108, 109, 110, 111, 112].s_reverse = 'ponml' and the ordinals are [112, 111, 110, 109, 108]. The absolute differences of the adjacent elements for both strings are [1, 1, 1, 1], so the answer is Funny.
Function Description

Complete the funnyString function in the editor below.

funnyString has the following parameter(s):

string s: a string to test
Returns

string: either Funny or Not Funny
Constraints
1 <= q <= 10
2 <= length of s <= 10000
"""
def funnyString(s):
    s_reverse = s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(s_reverse[i])-ord(s_reverse[i+1])):
            return 'Not Funny'
    return 'Funny'

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        print(result)
