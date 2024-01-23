"""
There is a sequence of words in CamelCase as a string of letters, s, having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given s, determine the number of words in s.
Example
s = oneTwoThree
There are 3 words in the string: 'one', 'Two', 'Three'.
Function Description

Complete the camelcase function in the editor below.

camelcase has the following parameter(s):

string s: the string to analyze
Returns

int: the number of words in s
Constraints
1 <= |s| <= 10^5
"""
def camelcase(s):
    # Write your code here
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count

if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)