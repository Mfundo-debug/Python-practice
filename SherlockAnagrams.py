"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
 Given a string,find the number of pairs of substrings of the string that are anagrams of each other.
 Example
 s = mom
The list of all anagrammatic pairs is [m,m],[mo,om] at positions [[0],[2]],[[0,1],[1,2]] respectively.
Function Description

Complete the function sherlockAndAnagrams in the editor below.

sherlockAndAnagrams has the following parameter(s):

string s: a string
Returns

int: the number of unordered anagrammatic pairs of substrings in s
Constraints
1<=q<=10
2<=|s|<=100
s contains only lowercase letters in the range ascii[a-z] 
"""

def sherlockAndAnagrams(s):
    n = len(s)
    count = 0
    for i in range(1,n):
        d = {}
        for j in range(n-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            if subs in d:
                count += d[subs]
                d[subs] += 1
            else:
                d[subs] = 1
    return count

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(result)