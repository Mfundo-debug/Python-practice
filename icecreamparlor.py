"""
Two friends like to pool their money and go to the ice cream parlor.
They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, 
select the two that will cost all of the money they have.
Example
m = 6 cost = [1, 3, 4, 5, 6]
The two flavors that cost 1 and 5 meet the criteria.
Using 1-based indexing, they are at indices 1 and 4.
Function Description

Complete the icecreamParlor function in the editor below.

icecreamParlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
Constraints
1 <= t <= 50
2 <= m <= 10^4
2 <= n <= 10^4
1 <= cost[i] <= 10^4, where i E [1, n]
"""
def icecreamParlor(m, arr):
    #write your code here
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i+1, j+1]
    return None
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        print(' '.join(map(str, result)))