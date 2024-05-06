"""
You are given an unordered array of unique integers incrementing from 1.
You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.
Example
arr = [1,2,3,4] 
k = 1

Function Description

Complete the largestPermutation function in the editor below. It must return an array that represents the highest value permutation that can be formed.

largestPermutation has the following parameter(s):

int k: the maximum number of swaps
int arr[n]: an array of integers

Constraints
1 <= n <= 10^5
1 <= k <= 10^9
"""

def largestPermutation(k, arr):
    n = len(arr)
    index = [0] * (n+1)
    for i in range(n):
        index[arr[i]] = i
    for i in range(n):
        if k == 0:
            break
        if arr[i] == n-i:
            continue
        arr[index[n-i]] = arr[i]
        index[arr[i]] = index[n-i]
        arr[i] = n-i
        index[n-i] = i
        k -= 1
    return arr

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(' '.join(map(str, result)))