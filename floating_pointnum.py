"""
You are given a string N.
Your task is to verify that N is a floating point number.
Input Format

The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Constraints
0 < T <10
"""
import re

def floating_pointnum():
    for _ in range(int(input())):
        print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

if __name__ =='__main__':
    floating_pointnum()