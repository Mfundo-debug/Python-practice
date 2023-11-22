"""
A driver is driving on the freeway. The check engine light of his vehicle is on, and the driver wants to get service immediately. 
Luckily, a service lane runs parallel to the highway. It varies in width along its length.
You will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points.
Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.
Example 
n =4
width = [2,3,2,1]
cases = [[1,2],[2,4],[2,4],[2,3]]
If the entry index, i=1 and the exit,j=2 , there are two segment widths of 2 and 3 respectively.
The widest vehicle that can fit through both is 2. If i=2 and j=4, the widths are [3,2,1] which limits vehicle width to 1.
Function Description

Complete the serviceLane function in the editor below.

serviceLane has the following parameter(s):

int n: the size of the width array
int cases[t][2]: each element contains the starting and ending indices for a segment to consider, inclusive
Returns

int[t]: the maximum width vehicle that can pass through each segment of the service lane described.
Constraints
2 <= n <= 1000
1 <= t <= 1000
0 <= i < j < n
2 <= j-i+1 <= min(n,1000)
1 <= width[k] <= 3, where 0 <= k < n
"""
def serviceLane(n, cases):
    result = []
    for i in range(len(cases)):
        result.append(min(width[cases[i][0]:cases[i][1]+1]))
    return result
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(n, cases)
    print('\n'.join(map(str, result)))
    print('\n')