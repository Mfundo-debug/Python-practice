"""
Consider the following:

A string, s, of length n where  s = c_0, c_1,...c_{n-1}.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, t_i, consists of a contiguous block of k characters in s.
 Then, use each u_i to create string  such that:

The characters in u_i are a subsequence of the characters in t_i.
Any repeat occurrence of a character is removed from the string such that each character u_i in  occurs exactly once. 
In other words, if the character at some index j in t_i occurs at a previous index < j in t_i, then do not include the character in string u_i.
Given s and k, print n/k lines where each line  denotes string u_i.

Example
s = `AAABCADDE`
k = 3

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so  u_i=`A`. 
The second substring has all distinct characters, so u_2=`BCA`. The third substring has 2 different characters, so u_3=`DE`. Note that a subsequence maintains the original order of characters encountered. 
The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format

The first line contains a single string, s.
The second line contains an integer,k , the length of each substring.

Constraints
1 <= n <= 10^4, where n is the length of s
1 <= k <= n
It is guaranteed that n is a multiple of k.
"""

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        t = string[i:i+k]
        u = ''
        for c in t:
            if c not in u:
                u += c
        print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)