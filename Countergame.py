"""
Louise and Richard have developed a numbers game. They pick a number and check to see if it a power of 2.
if it is they divide it by 2, if not they reduce it by the next lower number which is a power of 2.
Whoever reduces the number to 1 wins the game. Louise always starts.
Given an initial value, determine who wins the game.
Example
n = 132
It's Louise's turn. She determines that 132 is not a power of 2. The next lower power of 2 is 128, so she subtracts that from 132 and passes 4 to Richard.
4 is a power of 2, so Richard divides it by 2 and passes 2 to Louise.
Likewise, 2 is a power of 2 so Louise divides it by 2 and reaches 1.
Richard wins. Louise cannot make a move so she loses.
Update if they initially set counter to 1, Richard wins. Louise cannot make a move so she loses.
Function Description

Complete the counterGame function in the editor below.

counterGame has the following parameter(s):

int n: the initial game counter value
Returns
string: either Richard or Louise
Constraints
1 <= n <= 2^64 - 1
1 <= t <= 10
"""
def counterGame(n):
    counter = 0
    while n != 1:
        if n & (n - 1) == 0:
            n >>= 1
        else:
            n -= 2 ** (n.bit_length() - 1)
        counter += 1
    return 'Louise' if counter % 2 == 0 else 'Richard'

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = counterGame(n)
        print(result)