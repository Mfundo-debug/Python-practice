"""
Alice gives Bob a board composed 1x1 wooden squares and asks him to find the minimum cost of breaking the board back down into its individual squares. To break the board down, Bob must make cuts along its horizontal and vertical lines.

To reduce the board to squares, Bob makes horizontal and vertical cuts across the entire board. Each cut has a given cost, cost_y[i] or cost_x[j] for each cut along a row or column across onr board, so the cost
of a cust must be multiplied by the number of segements it crosses. The cost of cutting the whole board down in to 2x1 squares is the sum of the costs of each successive cut.
Can you help Bob find the minimum cost? The number may be large, so print the value modulo  10^9 + 7.
For example, you start with a 2 x 2 board. There are two cuts to be made at a cost of cost_y[1] = 3 for the horizontal and cost_x[1] = 1 for vertical. There are two cuts to be made at a cost of cost_y[1]=3 fpr tje horizontal and cost_x[1]=1 for vertical.
Your first cut is across 1 piece, the whole board. You choose to make the horizontal cut between rows 1 and 2 for a cost of 1 x 3 =3.
The second cuts are vertical through the two smaller boards created in step 1 between columns 1 and 2. Their cost is 2x1=2. The total cost is 3+2=5 and 5%(10^9 + 7) = 5.
FUnction Description:
Complete the boardCutting function in the editor below. It should return an integer.

boardCutting has the following parameter(s):

cost_x: an array of integers, the costs of vertical cuts
cost_y: an array of integers, the costs of horizontal cuts

Constraints:
1 <= q <= 20
2 <= n, m <= 10^5
0 <= cost_y[i], cost_x[i] <= 10^9
"""

def boardCutting(cost_x, cost_y):
    cost_x.sort(reverse=True)
    cost_y.sort(reverse=True)
    i = 0
    j = 0
    total_cost = 0
    horizontal_cuts = 1
    vertical_cuts = 1
    while i < len(cost_x) and j < len(cost_y):
        if cost_x[i] > cost_y[j]:
            total_cost += cost_x[i] * horizontal_cuts
            vertical_cuts += 1
            i += 1
        else:
            total_cost += cost_y[j] * vertical_cuts
            horizontal_cuts += 1
            j += 1
    while i < len(cost_x):
        total_cost += cost_x[i] * horizontal_cuts
        i += 1
    while j < len(cost_y):
        total_cost += cost_y[j] * vertical_cuts
        j += 1
    return total_cost % (10**9 + 7)
    

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n, m = map(int, input().split())
        cost_x = list(map(int, input().rstrip().split()))
        cost_y = list(map(int, input().rstrip().split()))
        result = boardCutting(cost_x, cost_y)
        print(result)