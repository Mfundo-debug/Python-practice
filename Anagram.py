"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. 
Determine the minimum number of characters to change to make the two substrings into anagrams of one another.
Example
 s = abccde
 Break s into two parts: abcd and cde. Note that all letters have been used, the substrings are contiguous and their lengths are equal.
Now you can change c and d in the second substring to a and b to have identical strings.
Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Constraints
1 <= |s| <= 10^4
1 <= q <= 100
"""
def anagram(s):
    if len(s)%2 != 0:
        return -1
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    s1 = list(s1)
    s2 = list(s2)
    count = 0
    for i in s1:
        if i in s2:
            s2.remove(i)
        else:
            count += 1
    return count

if __name__ == '__main__':
    s = input()
    result = anagram(s)
    print(result)