"""
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well.
In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.
Example
arr = [5, 2, 3, 4, 1]
sorted = [1, 2, 3, 4, 5]. Several pairs have the minimum difference of 1: [(1, 2), (2, 3), (3, 4), (4, 5)].
[(1,2),(2,3),(3,4),(4,5)]. Return the array [1,2,2,3,3,4,4,5].
Function Description

Complete the closestNumbers function in the editor below.

closestNumbers has the following parameter(s):

int arr[n]: an array of integers
Returns
- int[]: an array of integers as described
COnstraints
2 <= n <= 200000
-10^7 <= arr[i] <= 10^7
all arr[i] are unique in arr
"""

def closestNumbers(arr):
    arr.sort()
    min_diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr)-1):
        if abs(arr[i] - arr[i+1]) < min_diff:
            min_diff = abs(arr[i] - arr[i+1])
    result = []
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) == min_diff:
            result.append(arr[i])
            result.append(arr[i+1])
    return result
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)