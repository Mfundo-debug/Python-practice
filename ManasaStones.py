"""
Manasa is out on a hike with friends. She finds a trail of stones with numbers on them.
She starts following the trail and notices that any two consecutive stones' numbers differ by one of two values.
Legend has it that there is a treasure trove at the end of the trail. If Manasa can guess the value of the last stone, the treasure will be hers.
Example
 n = 2
 a =2
 b =3
She finds 2 stones and their differences are a=2 or b=3. We know she starts with a 0 stone not included in her count.
The permutations of differences for the two stones are [2,2],[2,3],[3,2] or [3,3]. 
Looking at each scenario, stones might have [2,4][2,5],[3,5] or [3,6] on them. The last stone might have any of 4,5 or 6 on its face.
Compute all possible numbers that might occur on the last stone given a starting stone with a 0 on it,
a number of additional stones found, and the possible differences between consecutive stones. Order the list ascending.

Function Description

Complete the stones function in the editor below.

stones has the following parameter(s):

int n: the number of non-zero stones
int a: one possible integer difference
int b: another possible integer difference
Returns

int[]: all possible values of the last stone, sorted ascending
Constraints
1 <= t <= 10
1 <= n,a,b <= 10^3
"""
import os
# Time Complexity: O(n)
# Space Complexity: O(n)
def stones(n, a, b):
    lastStone = []
    for i in range(n):
        lastStone.append(a*(n-1-i) + b*i)
    return sorted(set(lastStone))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()