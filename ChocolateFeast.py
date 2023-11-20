"""
Little Bobby loves chocolate. He frequently goes to his favorite 5&10 store, Penny Auntie, to buy them. 
They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.
Example
n = 15
c = 3
m = 2
He has 15 to spend, bars cost 3, and he can turn in 2 wrappers to receive another bar. 
Initially, he buys 5 bars and has 5 wrappers after eating them. He turns in 4 of them, leaving him with 1, for 2 more bars.
After eating those two, he has 3 wrappers, turns in 2 leaving him with 1 wrapper and his new bar.
Once he eats that one, he has 2 wrappers and turns them in for another bar.
After eating that one, he only has 1 wrapper, and his feast ends. Overall, he has eaten 5+2+1+1= 9 bars.
Function Description

Complete the chocolateFeast function in the editor below.

chocolateFeast has the following parameter(s):

int n: Bobby's initial amount of money
int c: the cost of a chocolate bar
int m: the number of wrappers he can turn in for a free bar
Returns

int: the number of chocolates Bobby can eat after taking full advantage of the promotion
Note: Little Bobby will always turn in his wrappers if he has enough to get a free chocolate.
Constraints
1<=t<=1000
2<=n<=10^5
1<=c<=n
2<=m<=n
"""
def chocolateFeast(n,c,m):
    # Write your code here
    choc = n//c
    wrap = choc
    while wrap >= m:
        choc += wrap//m
        wrap = wrap//m + wrap%m
    return choc
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        print(result)