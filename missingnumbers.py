"""
Given two arrays of integers, find which elements in the second array are missing from the first array.
Example
arr = [7, 2, 5, 3, 5, 3]
brr = [7, 2, 5, 4, 6, 3, 5, 3]
The arr array is the orginal list. The numbers missing are [4, 6].

Function Description

Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

missingNumbers has the following parameter(s):

int arr[n]: the array with missing numbers
int brr[m]: the original array of numbers
Returns
int[]: an array of integers
COnstraints
1 <= n, m <= 2 x 10^5
n <= m
1 <= brr[i] <= 10^4
max(brr) - min(brr) < 100
"""
def missingNumbers(arr,brr):
    arr.sort()
    brr.sort()
    missing = []
    i = 0
    j = 0
    while i < len(arr) and j < len(brr):
        if arr[i] == brr[j]:
            i += 1
            j += 1
        else:
            missing.append(brr[j])
            j += 1
    while j < len(brr):
        missing.append(brr[j])
        j += 1
    return sorted(set(missing))

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    brr_count = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    print(result)