"""
Function Description

Complete the findMedian function in the editor below.

findMedian has the following parameter(s):

int arr[n]: an unsorted array of integers
Returns

int: the median of the array
Constraints
1 <= n <= 1000001
n is odd
-10000 <= arr[i] <= 10000 where 0 <= i < n
"""
def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    print(result)