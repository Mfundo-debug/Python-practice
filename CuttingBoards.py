"""
Alice gives Bob a board composed of n x m squares. On each square there is a number. The board is divided into two parts by a single vertical or horizontal line. Bob's task is to cut the board exactly once in such a way that the sum of the numbers in the left part is equal to the sum of the numbers in the right part. Bob wants to minimize the absolute difference between the sums. Help Bob by finding this difference.
To reduce the board to squares, Bob must perform the following operation:
1. Choose a vertical or horizontal line that will cut the board into two parts.
2. The line can be placed between two columns or two rows, and can be placed anywhere in the board.
3. The line will cut all the squares it passes through.
4. The sum of all the numbers in the left part is calculated.
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
    # Write your code here
    cost_x.sort(reverse=True)
    cost_y.sort(reverse=True)
    x = 0
    y = 0
    result = 0
    while cost_x or cost_y:
        if cost_x and cost_y:
            if cost_x[0] >= cost_y[0]:
                x += 1
                result += cost_x[0] * y
                cost_x.pop(0)
            else:
                y += 1
                result += cost_y[0] * x
                cost_y.pop(0)
        elif cost_x:
            x += 1
            result += cost_x[0] * y
            cost_x.pop(0)
        else:
            y += 1
            result += cost_y[0] * x
            cost_y.pop(0)
    return result % (10**9 + 7)

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n, m = map(int, input().split())
        cost_x = list(map(int, input().rstrip().split()))
        cost_y = list(map(int, input().rstrip().split()))
        result = boardCutting(cost_x, cost_y)
        print(result)