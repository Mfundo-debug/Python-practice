"""
You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth.
 We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth.
Two cells are adjacent if they have a common side, or edge.
Find all the cavities on the map and replace their depths with the uppercase character X.
Example
grid = ['989', '191', '111']
Function Description

Complete the cavityMap function in the editor below.

cavityMap has the following parameter(s):

string grid[n]: each string represents a row of the grid
Returns

string{n}: the modified grid

Constraints
1 <= n <= 100
"""
def cavityMap(grid):
    n = len(grid)
    new_grid = grid.copy()
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if int(grid[i][j]) > max(int(grid[i - 1][j]), int(grid[i + 1][j]), int(grid[i][j - 1]), int(grid[i][j + 1])):
                new_grid[i] = new_grid[i][:j] + 'X' + new_grid[i][j + 1:]
    return new_grid
if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    print('\n'.join(result))
    print('\n')