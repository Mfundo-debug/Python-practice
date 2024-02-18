"""
Amanda has a string of lowercase letters that she wants to copy to a new string. 
She can perform the following operations with the given costs. She can perform them any number of times to construct a new string p:
* Append a character to the end of string p at a cost of 1 dollar.
* Choose any substring of p and append it to the end of p at no charge.
Givrn n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.
For example, given a string s = abcabc, it can be copied for 3 dollars. Start by copying a, b and c individually at a cost of 1 dollar per character. 
String p = abc at this time. Copy p[0:2] to the end of p at no cost to complete the copy.
Function Description

Complete the stringConstruction function in the editor below. It should return the minimum cost of copying a string.

stringConstruction has the following parameter(s):
s: a string
Constraints
1 <= n <= 5
1 <= |s[i]| <= 10^5
Subtasks
1 <= |s[i]| <= 10^3 for 45% of the maximum score.
"""
def stringConstruction(s):
    return len(set(s))

if __name__ == "__main__":
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        print(result)