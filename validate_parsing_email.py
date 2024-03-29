"""
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.
Given m pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge
nput Format

The first line contains a single integer, n, denoting the number of email address.
Each line  of the  subsequent lines contains a name and an email address as two space-separated values following this format:

name <user@email.com>

Constraints
0 < n < 100
"""
import re
import email.utils

n = int(input())

for i in range(n):
    name, email_address = input().split()
    if re.match(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email.utils.parseaddr(email_address)[1]):
        print(name, email_address)

