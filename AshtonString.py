"""
Ahton appeared for a job interview is asked the following question. Arrange all the distinct substrings of a given string in lexicographical order and concatenate them.
Print the kth character of the concatenated string. it is assuared that given value of k will be valid i.e there will be a kth character.
For example, given the string s = abc, its distinct substrings are
[a,ab,abc,abcd,b,bc,bcd,c,cd,d]. Sorted and concatenated, they make the string aababbcabcdbbcbcdccdd. if K = 5 then, the answer is b, the 5th character of 1-indexed concatenated string.
Note We have distinct substrings here, i.e. if string is aa, it's distinct substrings are a and aa.

Function Description

Complete the ashtonString function in the editor below. It should return the  character from the concatenated string, 1-based indexing.

ashtonString has the following parameters:
- s: a string
- k: an integer

Constraints
1 <= |s| <= 10^5
1 <= t <= 5
Eacch character of string s is a lowercase English letter ascii.
k will be an appropriate value for the given string s.
"""
def ashtonString(s, k):
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    substrings.sort()
    print(substrings)
    concatenated = ''.join(substrings)
    return concatenated[k-1]

if __name__ == '__main__':
    t = int(input().strip())
    for t_ir in range(t):
        s = input().strip()
        k = int(input().strip())
        result = ashtonString(s, k)
        print(result)