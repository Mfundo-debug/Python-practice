"""
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7,8 or 9.

Concept

A valid mobile number is a ten digit number starting with a 7,8 or 9.

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here.
You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Constraints
1 <= N <= 10
2 <= len(Number) <= 15
"""
import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        number = input()
        if re.match(r'[789]\d{9}$', number):
            print('YES')
        else:
            print('NO')
            