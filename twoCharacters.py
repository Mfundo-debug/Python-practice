"""
iven a string, remove characters until the string is made up of any two alternating characters. 
When you choose a character to remove, all instances of that character must be removed. 
Determine the longest string possible that contains just two alternating letters.
Example 
s = 'abaacdabd'
Delete a, to leave abacdabd. Now, remove character c to leave the valid string bdbd with a length of 4.
Removing either b or d at any point would not result in a valid string. Return 4.

Given a string s, convert it to the longest possible string t made up only of alternating characters.
Return the length of string t. If no string t can be formed, return 0.

Function Description

Complete the alternate function in the editor below.

alternate has the following parameter(s):

string s: a string
Returns.

int: the length of the longest valid string, or 0 if there are none
Constraints
1 <= |s| <= 1000
s[i] belongs to ascii[a-z]
"""
def alternate(s):
    if len(set(s)) == 1:
        return 0

    max_length = 0
    for i in range(26):
        for j in range(i+1, 26):
            c1 = chr(i + 97)
            c2 = chr(j + 97)
            last = ''
            length = 0
            for c in s:
                if c == c1 or c == c2:
                    if c == last:
                        length = 0
                        break
                    last = c
                    length += 1
            max_length = max(max_length, length)
    return max_length
    
    
if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    print(alternate(s))