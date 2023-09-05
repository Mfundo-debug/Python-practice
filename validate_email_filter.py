"""
You are given an integer N followed by N email addresses. 
Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores 
[a-z],[A-Z],[0-9],[_-].
The website name can only have letters and digits [a-z],[A-Z],[0-9] .
The extension can only contain letters[a-z][A-Z] .
The maximum length of the extension is 3.

Concept

A filter takes a function returning True or False and applies it to a sequence,
returning a list of only those members of the sequence where the function returned True.
A Lambda function can be used with filters.
Input Format

The first line of input is the integer N, the number of email addresses.
 lines follow, each containing a string.

Constraints

Each line is a non-empty string.


Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Expected Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""
def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False

    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())