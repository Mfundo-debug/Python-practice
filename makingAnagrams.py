"""
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency. 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Alice is taking a cryptography class and finding anagrams to be very useful. 
She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
Can you help her find this number?
Given two strings, s1 and s2, that may not be of the same length, determine the minimum number of character deletions required to make s1 and s2 anagrams.
Any characters can be deleted from either of the strings
Example
s1 = abc
s2 = amnop
The only characters that match are a's so we have to remove bc from s1 and mnop from s2 for a total of 6 deletions.
Function Description
Complete the makingAnagrams function in the editor below.

makingAnagrams has the following parameter(s):

string s1: a string
string s2: a string
Returns

int: the minimum number of deletions needed
Constraints
1 ≤ |s1|, |s2| ≤ 10^4
"""

def makingAnagrams(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    count = 0
    for i in s1:
        if i in s2:
            s2.remove(i)
        else:
            count += 1
    return count + len(s2)

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1,s2)
    print(result)