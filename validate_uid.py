"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z , A - Z  & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.

Input Format
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID

Output Format
For each test case, print 'Valid' if the UID is valid.
Otherwise, print 'Invalid', on separate lines. 
Do not print the quotation marks.
"""
import string

if __name__ == '__main__':
    for _ in range(int(input())):
        uid = input()
        if len(uid) == 10 and uid.isalnum() and sum(c.isupper() for c in uid) >= 2 and sum(c.isdigit() for c in uid) >= 3 and not any(uid.count(c) > 1 for c in uid):
            print('Valid')
        else:
            print('Invalid')
            