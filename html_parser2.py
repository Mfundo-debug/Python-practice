"""
Task

You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.
Note: Do not print data if data == '\n'.

Input Format

The first line contains integer N, the number of lines in the HTML code snippet.
The next N lines contains HTML code.

Constraints
0 < N < 100
"""
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    
    def handle_data(self, data):
        if data.strip() and data != '\n':
            print('>>> Data')
            print(data)

if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
    
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()