"""
We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. 
Remeber that a subsequence maintains the order of characters selected from a sequence.
More formally, let p[0], p[1], ... p[9] be the respective indices of h, a, c, k, e, r, r, a, n, k in string s.
If p[0] < p[1] < p[2] < ... < p[9] is true, then s contains hackerrank.
For each query, we return YES if the string contains hackerrank, otherwise, we return NO.
Function Description

Complete the hackerrankInString function in the editor below.

hackerrankInString has the following parameter(s):

string s: a string
Returns

string: YES or NO
Constraints
2 ≤ |s| ≤ 10^4
10 <= |s| <= 10^4
"""
def hackerRankInString(s):
    word = 'hackerrank'
    for i in s:
        if i == word[0]:
            word = word[1:]
        if len(word) == 0:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    s = input()
    result = hackerRankInString(s)
    print(result)