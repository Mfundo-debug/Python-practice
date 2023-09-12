"""
Task

You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.
that has consecutive repetitions.
Input Format

A single line of input containing the string S.

Constraints
0 < len(S) < 100
"""
import re

def group_func(string):
    match = re.search(r'([a-zA-Z0-9])\1+', string)
    print(match.group(1) if match else -1)

if __name__ == '__main__':
    string = input()
    group_func(string)