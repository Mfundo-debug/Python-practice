"""
Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:
i < j < k
a[j] - a[i] = a[k] - a[j] = d
Given an increasing sequence of integers and the value of d, count the number of beautiful triplets in the sequence.
Example
arr = [2, 2, 3, 4, 5]
d = 1
There are three beautiful triplets, by index: [i, j, k] = [0, 2, 3], [1, 2, 3], [2, 3, 4]. 
To test the first triplet, arr[j] - arr[i] = 3 - 2 = 1 and arr[k] - arr[j] = 4 - 3 = 1.
Function Description

Complete the beautifulTriplets function in the editor below.

beautifulTriplets has the following parameters:

int d: the value to match
int arr[n]: the sequence, sorted ascending
Returns

int: the number of beautiful triplets
Constraints
1 <= n <= 10^4
1 <= d <= 20
0 <= arr[i] <= 2 * 10^4
arr[i] > arr[i-1] for 1 <= i <= n
"""
def beautifulTriplets(d,arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            count += 1
    return count
if __name__ == '__main__':
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    print(beautifulTriplets(d,arr))