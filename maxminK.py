"""
You will be given a list of integers, arr, and a single integer k. you must create an array of length k from elements of arr such
that its unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as:
max(subarr) - min(subarr)
Where:
- max denotes the largest integer in subarr
- min denotes the smallest integer in subarr
Example
arr = [1, 4, 7, 2]
k = 2
Pick any two elements, test subarr = [4, 7]
unfairness = max(4, 7) - min(4, 7) = 3
Testing for all pairs, the solution [1, 2] provides the minimum unfairness.
Function Description

Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness

Constraints
2 <= n <= 10^5
2 <= k <= n
0 <= arr[i] <= 10^9
"""

def maxMin(k, arr):
    arr.sort()
    min_unfairness = float('inf')
    for i in range(len(arr)-k+1):
        min_unfairness = min(min_unfairness, arr[i+k-1] - arr[i])
    return min_unfairness

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    print(result)