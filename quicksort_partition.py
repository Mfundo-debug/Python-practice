"""
Step 1: Divide
Choose some pivot element, p, and partition your unsorted array, arr, into three smaller arrays: 
left, right, and equal, where each element in left < p, each element in right > p, and each element in equal = p.
Example
arr = [5, 7, 4, 3, 8]
pivot = arr[0] = 5
Function Description

Complete the quickSort function in the editor below.

quickSort has the following parameter(s):

int arr[n]:arr[0]  is the pivot element
Returns

int[n]: an array of integers as described above
Constraints
1 <= n <= 1000
-1000 <= arr[i] <= 1000 where 0 <= i < n
All elements will be unique.
"""
def quicksort(arr):
    left = []
    right = []
    equal = []
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return left + equal + right
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quicksort(arr)
    print(' '.join(map(str, result)))