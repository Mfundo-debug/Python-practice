"""
Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices. 
 has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
 Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
Note Each toy can be purchased only once.
Example
prices = [1,2,3,4]
k = 7
the budget is 7 units of currency. He can buy items that cost [1,2,3] for 6, or [3,4] for 7 units.
The maximum is 3 items.
Function Description

Complete the function maximumToys in the editor below.

maximumToys has the following parameter(s):

int prices[n]: the toy prices
int k: Mark's budget
Returns

int: the maximum number of toys

Constraints
1 <= n <= 10^5
1 <= k <= 10^9
1 <= prices[i] <= 10^9
A toy can't be bought multiple times.
"""

def maximumToys(prices, k):
    prices.sort()
    count = 0
    for i in prices:
        if k > i:
            k -= i
            count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)