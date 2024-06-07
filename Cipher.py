"""
Jack and Daniel are friends. They want to encrypt their conversation so that they can save themselves from interception by a detective agency. So they invent a new cipher.
Every message is encoded to its binary representation B of length N. Then it is written down K times, shifted by an offset. If B = 1001010 and K = 4 it looks like:
1001010 shift 0
0100101 shift 1
0010010 shift 2
0001001 shift 3
Now we calculate the XOR of the values at the same position and write it down.
So the result of the above example is:
1110010

Function Description

Complete the cipher function in the editor below. It should return the decoded string.

cipher has the following parameter(s):

k: an integer that represents the number of times the string is shifted
s: an encoded string of binary digits

Constraints
1 <= n <= 10^6
1 <= k <= 10^6
|s| = n + k - 1
it is guaranteed that the string is a valid encoded binary string.
"""
def cipher(n, k, s):
    res = [0] * n
    xor = 0
    for i in range(n + k - 1):
        xor ^= int(s[i])
        if i >= n:
            xor ^= res[i - n]
        res[i % n] = xor
    return ''.join(map(str, res))

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()
    result = cipher(n, k, s)
    print(result)