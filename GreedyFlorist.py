"""
A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1.
The first flower will be original price, (0+1) x original price, the next will be (1+1) x original price and so on.
Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers.
The number of flowers they want equals the length of the c array.
Example
c=[1,2,3,4]
k=3
The length of c array is 4, so they want to buy 4 flowers. The first flower will cost 1, the second will cost (0+1) x 2=2, the third will cost (1+1) x 3=6, and the fourth will cost (2+1) x 4=12. The total cost is 1+2+6+12=21.
Function Description
Function Description

Complete the getMinimumCost function in the editor below.


getMinimumCost has the following parameter(s):

int c[n]: the original price of each flower
int k: the number of friends
Constraints
1 <= n,k <= 100
1 <= c[i] <= 10^6
answer < 2^31
0 <= i < n
"""
def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    for i in range(len(c)):
        cost += (i//k + 1) * c[i]
    return cost

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)