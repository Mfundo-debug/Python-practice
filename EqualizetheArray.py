"""
Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.
Example 
arr = [1,2,2,3]
Delete the 2 elements 1 and 3 leaving arr = [2,2]. If both twos plus either the 1 or the 3 are deleted, it takes 3 deletions to leave either [3] or [1]. 
The minimum number of deletions is 2.
Function Description

Complete the equalizeArray function in the editor below.

equalizeArray has the following parameter(s):

int arr[n]: an array of integers
Returns

int: the minimum number of deletions required
Input Format

The first line contains an integer n, the number of elements in arr.
The next line contains n space-separated integers arr[i].

Constraints
1 <= n <= 100
1 <= arr[i] <= 100
"""
def equalizeArray(arr):
    # Write your code here
    # create a dictionary to store the count of each element
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # find the max value in the dictionary
    max_val = max(d.values())
    # return the length of the array minus the max value
    return len(arr) - max_val
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()