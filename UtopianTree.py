"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. 
Each summer, its height increases by 1 meter.
A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. 
How tall will the tree be after n growth cycles?
Function Description

Complete the utopianTree function in the editor below.

utopianTree has the following parameter(s):

int n: the number of growth cycles to simulate
Returns

int: the height of the tree after the given number of cycles
Input Format

The first line contains an integer, t, the number of test cases.
t subsequent lines each contain an integer, n, the number of cycles for that test case.
Constraints
1 <= t <= 10
0 <= n <= 60
"""
def utopianTree(n):
    height = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2
    return height
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        print(result)
    
