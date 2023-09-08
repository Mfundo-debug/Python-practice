"""
You are given a string .
S contains alphanumeric characters only.
 Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints
0 < len(S) < 1000
"""
def sorting(S):
    lower = []
    upper = []
    odd = []
    even = []
    for i in S:
        if i.islower():
            lower.append(i)
        elif i.isupper():
            upper.append(i)
        elif i.isdigit():
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
    lower.sort()
    upper.sort()
    odd.sort()
    even.sort()
    return "".join(lower) + "".join(upper) + "".join(odd) + "".join(even)

if __name__ == '__main__':
    S = input()
    print(sorting(S))