"""
Sherlock is given 2vsquare tiles, intially both of whose sides have a length l placed in an x-y plane.
Initially, the bottom left corners of each square are the origin and their sides are parallel to the axes.
at t=0, both squares start moving along line y=x (along the positive x and y) with velocities s1 and s2.
For each query of form qi, Sherlock has to report the time at which the overlapping area of tiles is equal to qi.
Note: Assume all distances are in meters, and time is in seconds, and velocities in meters per second.

Function Signature: def movingTiles(l, s1, s2, queries)
movingTiles has the following parameter(s):

int l: side length for the two squares
int s1: velocity of square 1
int s2: velocity of square 2
int queries[q]: the array of queries
Returns

int[n]: an array of answers to the queries, in order. Each answer will be considered correct if it is at most  away from the true answer.

Constraints:
1 <= l,s1, s2 <= 10^9
1 <= q <= 10^5
1 <= queries[i] <= 10^9
s1 != s2
"""

def movingTiles(l, s1, s2, queries):
    # Write your code here
    result = []
    for q in queries:
        result.append((l * 2 ** 0.5 - ((s1 - s2) ** 0.5) * q) / abs(s1 - s2))
    return result

if __name__ == '__main__':
    m = input().rstrip().split()
    l = int(m[0])
    s1 = int(m[1])
    s2 = int(m[2])
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = movingTiles(l, s1, s2, queries)
    print('\n'.join(map(str, result)))