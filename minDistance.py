"""
The distance between two array values is the number of indices between them. 
Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1.
Example
a = [3,2,1,2,3]
There are two matching pairs of values: 3 and 2. The indices of the 3's are i = 0 and j = 4, so their distance is d[i,j] = |j - i| = 4.
The indices of the 2's are i = 1 and j = 3, so their distance is d[i,j] = |j - i| = 2.
The minimum distance is 2.
Function Description

Complete the minimumDistances function in the editor below.

minimumDistances has the following parameter(s):

int a[n]: an array of integers
Returns

int: the minimum distance found or -1 if there are no matching elements.
Constraints
1 <= n <= 10^3
0 <= a[i] <= 10^5  
"""
def minimumDistance(a):
    # Write your code here
    minDistance = -1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                if minDistance == -1:
                    minDistance = abs(j-i)
                else:
                    minDistance = min(minDistance, abs(j-i))
    return minDistance
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistance(a)
    #fptr.write(str(result) + '\n')
   # fptr.close()