"""
A person is getting ready to leave and needs a pair of matching socks. If there are  colors of socks in the drawer, how many n socks need to be removed to be certain of having a matching pair?
Example n = 2
There are 2 colors of socks in the drawer. If they remove 2 socks, they may not match. The minimum number to insure success is 3.

Function Description

Complete the maximumDraws function in the editor below.

maximumDraws has the following parameter:

int n: the number of colors of socks

Returns

int: the minimum number of socks to remove to guarantee a matching pair.

Constraints:
1 <= t <= 1000
0 <= n <= 10^6
"""

def maximumDraws(n):
    return n + 1

if __name__ == '__main__':
    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())
        result = maximumDraws(n)
        print(result)