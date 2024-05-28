"""
You will be given a list of 32 bit unsigned integers. Flip all the bits (1 to 0 and 0 to 1) and print the result as an unsigned integer.

Example
n = 9_10
9_10 = 1001_2. We're working with 32 bits, so:
00000000000000000000000000001001_2 = 9_10
11111111111111111111111111110110_2 = 4294967286_10
Return 4294967286.
Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns

int: the unsigned decimal integer result

Constraints
1 <= q <= 100
0 <= n <= 2^32
"""
def flippingBits(n):
    return n ^ 0xFFFFFFFF

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(result)