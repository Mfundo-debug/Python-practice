"""
Given a string, determine if it can rearranged inti a palindrome. Return the string YES or NO.
Example
s = 'aabbccdd'
One way this can be arranged into a palindrome is: abcdcba. Return YES.
Function Description
Complete the gameOfThrones function below.

gameOfThrones has the following parameter(s):

string s: a string to analyze
Returns

string: either YES or NO
Input Format

A single line which contains s, the input string.
Constraints
1 ≤ |s| ≤ 10^5
s will consist of lowercase letters in the range ascii[a-z].
"""
def gameOfThrones(s):
    # Count the frequency of each character in the string
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check if the string can be rearranged into a palindrome
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return "NO"
    
    return "YES"
if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)