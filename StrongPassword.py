"""
Louise joined a social networking site to stay in touch with her friends. 
The signup page required her to input a name and a password. 
However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:
* Its length is at least 6.
* It contains at least one digit.
* It contains at least one lowercase English character.
* It contains at least one uppercase English character.
* It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length n in the password field but wasn't sure if it was strong. 
Given the string she typed, can you find the minimum number of characters she must add to make her password strong?
Function Description

Complete the minimumNumber function in the editor below.

minimumNumber has the following parameters:

int n: the length of the password
string password: the password to test
Returns

int: the minimum number of characters to add
Constraints
1 <= n <= 100
All characters in password are in [a-z, A-Z, 0-9, !@#$%^&*()-+].
"""
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    if not any(i.isdigit() for i in password):
        count += 1
    if not any(i.islower() for i in password):
        count += 1
    if not any(i.isupper() for i in password):
        count += 1
    if not any(i in "!@#$%^&*()-+" for i in password):
        count += 1
    return max(count, 6 - n)

if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)