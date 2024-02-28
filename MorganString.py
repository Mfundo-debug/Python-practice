"""
Jack and Daniel are friends. Both of them like letters, especially uppercase ones.
They are cutting uppercase letters from newspapers, and each one of them has his collection of letters stored in a stack.

One beautiful day, Morgan visited Jack and Daniel. He saw their collections.
He wondered what is the lexicographically minimal string made of those two collections. 
He can take a letter from a collection only when it is on the top of the stack. Morgan wants to use all of the letters in their collections.
As an example, assume Jack has collected a = [A,C,A] and Daniel has b = [B,C,F]. The examples shows the top at index 0 for each stack of letters.

Function Description

Complete the morganAndString function in the editor below.

morganAndString has the following parameter(s):

string a: Jack's letters, top at index 
string b: Daniel's letters, top at index 
Returns
- string: the completed string
Constraints
1 <= |a|, |b| <= 10^5
1 <= T <= 5
a and b contain upper-case letters only, ascii[A-Z]
"""

def morganAndString(a, b):
    result = ''
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i:] < b[j:]:
            result += a[i]
            i += 1
        elif a[i:] > b[j:]:
            result += b[j]
            j += 1
        else:
            # Look ahead to the next unequal characters
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i+k] == b[j+k]:
                k += 1
            if j + k == len(b) or (i + k < len(a) and a[i+k] < b[j+k]):
                result += a[i]
                i += 1
            else:
                result += b[j]
                j += 1

    # Append the remaining characters of a and b to the result
    if i < len(a):
        result += a[i:]
    if j < len(b):
        result += b[j:]

    return result 

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        a = input()
        b = input()
        result = morganAndString(a, b)
        print(result)