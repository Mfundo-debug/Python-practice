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
def foo(text, k):
    stack = [("",list(range(len(text))))]
    while stack != []:
        prefix,ii = stack.pop()
        if k<len(prefix):
            return prefix[k]
        k -= len(prefix)
        cs = sorted([(text[i],i+1) for i in ii if i<len(text)], reverse=True)
        i = 0
        while i<len(cs):
            c = cs[i][0]
            ii2 = [cs[i][1]]
            j = i+1
            while j<len(cs) and cs[j][0]==c:
                ii2.append(cs[j][1])
                j+=1
            stack.append((prefix+c, ii2))
            i=j
    return None

T = int(input().strip())
for i in range(T):
    text = input().strip()
    k = int(input().strip())
    print(foo(text,k-1))