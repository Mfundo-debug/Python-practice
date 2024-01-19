"""
Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
Example
k =1 
arr = [1,2,3,4]
There are three values that diffr by k=1:2-1=1, 3-2=1, and 4-3=1. Return 3.
Function Description

Complete the pairs function below.

pairs has the following parameter(s):

int k: an integer, the target difference
int arr[n]: an array of integers
Returns

int: the number of pairs that satisfy the criterion

Constraints
2 <= n <= 10^5
0 < k < 10^9
0 < arr[i]<2^31 -1 
"""
def pairs(k, arr):
    # Write your code here
    # sort the array
    # iterate through the array
    # if the difference between the current element and the next element is equal to k
    # increment the count
    # return the count
    arr.sort()
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] == k:
                count += 1
                break
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)
    