"""
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String
Example
s = 'aab'
aab -> b
b -> Empty String
Function Description

Complete the superReducedString function in the editor below.

superReducedString has the following parameter(s):

string s: a string to reduce
Returns

string: the reduced string or Empty String
Constraints
1 <= length of s <= 100
"""
def superReducedString(s):
    # Write your code here
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack) or 'Empty String'

if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    print(result)