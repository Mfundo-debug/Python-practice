"""
Animesh has n empty candy jars, numbered from 1 to n, with infinite capacity. He performs m operations. 
Each operation is described by 3 integers, a, b, and k. Here, a and b are indices of the jars, and k is the number of candies to be added inside each jar whose index lies within the range [a, b] (both inclusive).
Can you tell the average number of candies after m operations?
Example
n = 5
operations = [[1,2,10],[3,5,10]]
The array has 5 elements that all start at 0. In the first operation, add 10 to rthe first 2 elements. Now the array is [10, 10, 0, 0, 0]. In the second operation, add 10 to the last 3 elements. Now the array is [10, 10, 10, 10, 10]. The average is (10+10+10+10+10)/5 = 10.

Function Description
Complete the solve function in the editor below.

solve has the following parameters:

int n: the number of candy jars
int operations[m][3]: a 2-dimensional array of operations
Returns

int: the floor of the average number of canidies in all jars.
Constraints
3 ≤ n ≤ 10^7
1 ≤ m ≤ 10^5
1 ≤ a ≤ b ≤ N
0 ≤ k ≤ 10^6
"""

def solve(n, operations):
    total = 0
    for a, b, k in operations:
        total += (b - a + 1) * k
    return total // n

if __name__ == '__main__':
    n, m = map(int, input().split())
    operations = [list(map(int, input().split())) for _ in range(m)]
    print(solve(n, operations))