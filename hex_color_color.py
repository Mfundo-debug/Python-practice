"""
You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, 
in order of their occurrence from top to bottom.
Input Format

The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

Constraints
0 < N < 50
"""

import re

n = int(input())
for _ in range(n):
    line = input()
    for color in re.findall(r'(?<!^)(?<!\w)#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})(?!\w)', line):
        print('#'+color)

