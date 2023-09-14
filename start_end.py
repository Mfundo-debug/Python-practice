"""
Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

Constraints
0 < len(S) < 100
0 < len(k) < len(S)
"""
import re

def start_end():
    S = input()
    k = input()
    pattern = re.compile(k)
    m = pattern.search(S)
    if not m:
        print("(-1, -1)")
    while m:
        print("({0}, {1})".format(m.start(), m.end() - 1))
        m = pattern.search(S, m.start() + 1)

if __name__ == '__main__':
    start_end()
    