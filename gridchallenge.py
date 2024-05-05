"""
Gien a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
Example
grid =['abc', 'ade', 'efg']
The grid rearranged to abc, ade, efg results in a column that is ordered top to bottom. The answer is YES.
Function Description

Complete the gridChallenge function in the editor below.

gridChallenge has the following parameter(s):

string grid[n]: an array of strings
Returns

string: either YES or NO
Constraints
1<= t <= 100
1 <= n <= 100
"""

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if grid[j][i] > grid[j+1][i]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)
        print(result)