"""
Challenge- Counting Sort Principle
Given an unsorted list of integers, use the counting sort method to sort the list and then print the sorted list.

Hint: You can use your previous code that counted the items to print out the actual values in order.

Function Description

Complete the countingSort function in the editor below. It should return the original array, sorted ascending, as an array of integers.

countingSort has the following parameter(s):

arr: an array of integers
Constraints
0 <= n <= 1000000
0 <= arr[i] < 100
"""
def countingSort(arr):
    #use sorted() to sort the list and print the sorted list
    return sorted(arr)

if __name__ =='__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(result)
