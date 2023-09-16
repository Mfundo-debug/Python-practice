"""
Task

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format

The first line contains the integer, N.
The next N lines each contain a line of the text.

Constraints
0 < N < 100
Neither && nor || occur in the start or end of each line
"""
import re

for _ in range(int(input())):
    line = input()
    line = re.sub(r'(?<= )(&&)(?= )', 'and', line)
    line = re.sub(r'(?<= )(\|\|)(?= )', 'or', line)
    print(line)

if __name__ == '__main__':
    pass