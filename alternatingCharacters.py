"""
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletion
Example
s = AABBAAAB
Remove an A at positions 0 and 3 to make s = ABAB
Function Description

Complete the alternatingCharacters function in the editor below.

alternatingCharacters has the following parameter(s):

string s: a string
Returns

int: the minimum number of deletions required
Constraints
1 <= q <= 10
1 <= |s| <= 10^5
"""
def alternatingCharacters(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
    return count

if __name__ == "__main__":
    s = input()
    result = alternatingCharacters(s)
    print(result)