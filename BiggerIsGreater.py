"""
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
Example
w =abcd
The next largest word is abdc.
Function Description

Complete the biggerIsGreater function in the editor below.

biggerIsGreater has the following parameter(s):

string w: a word
Returns
- string: the smallest lexicographically higher string possible or no answer
Constraints
1 <= T <= 10^5
1 <= |w| <= 100
w will contain only letters in the range ascii[a..z].
"""
def biggerIsGreater(w):
    # Write your code here
    w = list(w)
    i = len(w) - 1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    j = len(w) - 1
    while w[j] <= w[i-1]:
        j -= 1
    w[i-1], w[j] = w[j], w[i-1]
    w[i:] = w[len(w)-1:i-1:-1]
    return "".join(w)

if __name__ == '__main__':
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        print(result)