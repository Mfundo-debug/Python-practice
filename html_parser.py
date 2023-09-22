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
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for attr in attrs:
            print('->', attr[0], '>', attr[1])
    
    def handle_endtag(self, tag):
        print('End   :', tag)
    
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for attr in attrs:
            print('->', attr[0], '>', attr[1])

if __name__ == '__main__':
    n = int(input())
    html = ''
    for _ in range(n):
        html += input()
    parser = MyHTMLParser()
    parser.feed(html)