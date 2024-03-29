"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. 
He wants to verify whether his credit card numbers are valid or not.
 You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Input Format

The first line of input contains an integer N.
The next N lines contain credit card numbers.

Constraints
0 < N < 100
"""
def validate_credit_card():
    import re
    n = int(input())
    for _ in range(n):
        s = input()
        if re.match(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', s) and not re.search(r'(\d)\1{3,}', s.replace("-", "")):
            print("Valid")
        else:
            print("Invalid")

if __name__ == '__main__':
    validate_credit_card()