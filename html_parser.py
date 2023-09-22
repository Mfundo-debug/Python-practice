"""
Task

You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately

Input Format

The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.

Constraints
0 < N < 100
"""
import re 

def html_parser(html):
    pattern = r'<(\w+)(.*?)>'
    match = re.findall(pattern, html)
    for m in match:
        print('Start :', m[0])
        if m[1]:
            attr = re.findall(r'(\w+)=[\'\"](.*?)[\'\"]', m[1])
            if attr:
                for a in attr:
                    print('->', a[0], '>', a[1])
            else:
                print('->', m[1].strip(), '>', 'None')
        else:
            print('Empty :', m[0])
        print('End   :', m[0])
    return

if __name__ == '__main__':
    n = int(input())
    html = ''
    for _ in range(n):
        html += input()
    html_parser(html)