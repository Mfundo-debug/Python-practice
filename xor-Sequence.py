"""
An array, A, is defined as follows:
A[0] = 0
A[x] = A[x-1] ^ x for x > 0, where ^ denotes bitwise XOR
You will be given a left and right index, l and r. You must determine the XOR sum of the segment of A from l to r, inclusive.
A[l] ^ A[l+1] ^ ... ^ A[r] = A[l, r]
For example, A = [0,1,3,0,4,1,7,0,8]. The segment from l=1 to r=4 sums to 1^3^0^4 = 6.
Function Description

Complete the xorSequence function in the editor below. It should return the integer value calculated.

xorSequence has the following parameter(s):

l: the lower index of the range to sum
r: the higher index of the range to sum
Constraints
1 ≤ l ≤ r ≤ 10^15
1 < q ≤ 10^5
"""
def xorSequence(l, r):
    def xor(n):
        if n % 8 == 0 or n % 8 == 1:
            return n
        if n % 8 == 2 or n % 8 == 3:
            return 2
        if n % 8 == 4 or n % 8 == 5:
            return n + 2
        if n % 8 == 6 or n % 8 == 7:
            return 0
    return xor(r) ^ xor(l - 1) if l > 0 else xor(r)
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        lr = input().split()
        l = int(lr[0])
        r = int(lr[1])
        result = xorSequence(l, r)
        print(result)