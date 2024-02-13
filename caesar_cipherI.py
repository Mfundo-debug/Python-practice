"""
encrypts a message using the caesar cipher
Example
s = 'There's-a-starman-waiting-in-the-sky'
k = 3
The alphabet is rotated by 3 characters. The encrypted string is 'Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb'.
Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string
Constraints
1 <= n <= 100
0 <= k <= 100
s is a valid ASCII string without any spaces.
"""
import math, re

def caesarCipher(s, k):
    k = k % 26
    encrypted = ''
    for c in s:
        if re.match('[a-zA-Z]', c):
            if c.islower():
                encrypted += chr((ord(c) - 97 + k) % 26 + 97)
            else:
                encrypted += chr((ord(c) - 65 + k) % 26 + 65)
        else:
            encrypted += c
    return encrypted

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    print(caesarCipher(s, k))