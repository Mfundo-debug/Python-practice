"""
Task
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string .

Constraints
0 < len (S) < 100
"""
import re

def findall_iter(S):
    """
    >>> findall_iter('rabcdeefgyYhFjkIoomnpOeorteeeeet')
    ['ee', 'Ioo', 'Oeo', 'eeeee']
    """
    return re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', S, re.I)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    S = input()
    print(*findall_iter(S), sep='\n')



