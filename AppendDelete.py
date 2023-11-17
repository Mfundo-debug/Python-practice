"""
You have two strings of lowercase English letters. You can perform two types of operations on the first string:

Append a lowercase English letter to the end of the string.
Delete the last character of the string. Performing this operation on an empty string results in an empty string.
Given an integer,k , and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. 
If it's possible, print Yes. Otherwise, print No.
Example 
s = [a,b,c]
t = [d,e,f]
k =6

To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order.
On the 6th move, you will have the matching string. Return Yes.

If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string.
If there were fewer than 6 moves, we would not have succeeded in creating the new string.

Function Description

Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

appendAndDelete has the following parameter(s):

string s: the initial string
string t: the desired string
int k: the exact number of operations that must be performed
Returns

string: either Yes or No

Constraints
1<=|s|<=100
1<=|t|<=100
1<=k<=100
s and t consist of lowercase English alphabetic letters, ascii[a-z].
"""

def appendAndDelete(s,t,k):
    if len(s)+len(t)<=k:
        return 'Yes'
    else:
        for i in range(min(len(s),len(t))):
            if s[i]!=t[i]:
                break
        if (len(s)-i)+(len(t)-i)<=k and (len(s)-i)+(len(t)-i)%2==k%2:
            return 'Yes'
        else:
            return 'No'
        
if __name__=='__main__':
    s=input()
    t=input()
    k=int(input())
    result=appendAndDelete(s,t,k)
    print(result)