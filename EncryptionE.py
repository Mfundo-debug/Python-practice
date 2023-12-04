"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:
floor(sqrt(L)) <= row <= column <= ceil(sqrt(L)) where floor(x) is floor function and ceil(x) is ceil function
Example
s = if man was meant to stay on the ground god would have given us roots
After removing spaces, the string is 54 characters long. sqrt(54) is between 7 and 8,
so it is written in the form of a grid with 7 rows and 8 columns.
Ensure that rows x columns >= L
if multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows x columns.

The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

Create a function to encode a message.

Function Description

Complete the encryption function in the editor below.

encryption has the following parameter(s):

string s: a string to encrypt
Returns

string: the encrypted string

Constraints
1 <= |s| <= 81
s contains characters in the range ascii[a-z] and space, ascii(32).
"""
import math

def encryption(s):
    # remove spaces from the string
    s = s.replace(' ', '')
    # calculate the number of rows and columns
    rows = math.floor(math.sqrt(len(s)))
    columns = math.ceil(math.sqrt(len(s)))
    # if rows x columns is less than the length of the string, increase the number of rows
    if rows * columns < len(s):
        rows += 1
    # split the string into rows
    result = []
    for i in range(rows):
        result.append(s[i * columns : (i + 1) * columns])
    # loop through the columns and print the characters
    encoded_message = ''
    for i in range(columns):
        for j in range(rows):
            # check if the index is valid
            try:
                encoded_message += result[j][i]
            except IndexError:
                pass
        encoded_message += ' '
    return encoded_message

if __name__ == '__main__':
    s = input()
    print(encryption(s))
