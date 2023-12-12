"""
In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.

Example.
n = 7
arr = [3,4,7,5,6,2,1]
unction Description

Complete the insertionSort2 function in the editor below.

insertionSort2 has the following parameter(s):

int n: the length of arr[n]
int arr[n]: an array of integers
Constraints
1 <= n <= 1000
-10000 <= arr[i] <= 10000, 0<=i<n
"""
def insertionSort2(n,arr):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
