"""
omparison Sorting
Quicksort usually has a running time of n x log(n), but is there an algorithm that can sort even faster?
In general, this is not possible. Most sorting algorithms are comparison sorts, i.e.they sort a list just by comparing the elements to one another.
A comparison sort algorithm cannot beat n x log(n) (worst-case) running time, since n x log(n) represents the minimum number of comparisons needed to know where to place each element.
lternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort.
Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
Example
arr = [1,1,3,2,1]
All of the values are in the range [0...3], so create an array of zeroes, result = [0,0,0,0].
Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.

Function Description

Complete the countingSort function in the editor below.

countingSort has the following parameter(s):

arr[n]: an array of integers
Returns

int[100]: a frequency array
Constraints
100 <= n <= 10^6
0 <= arr[i] < 100 where 0 <= i < n
"""
def countingSort(arr):
    # Write your code here
    result = [0] * 100
    for i in arr:
        result[i] += 1
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(' '.join(map(str, result)))
    print('\n')