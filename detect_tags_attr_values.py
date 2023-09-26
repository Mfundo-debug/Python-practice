"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.
The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

Input Format
The first line contains an integer N, the number of lines in the HTML code snippet.
The next N lines contain HTML code.

Constraints
0 < N < 100
"""
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('->', attr[0], '>', attr[1])


if __name__ == '__main__':
    parser = MyHTMLParser()
    parser.feed(''.join([input().strip() for _ in range(int(input()))]))
    parser.close()