"""
Consider an array of numeric strings where each string is a positive number with anywhere from 1 to 10^6 digits.
Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of the sorted array on a new line.
Example
unsorted = ['1', '200', '150', '3']
Return the array ['1', '3', '150', '200'].
Function Description

Complete the bigSorting function in the editor below.

bigSorting has the following parameter(s):

string unsorted[n]: an unsorted array of integers as strings
Returns

string[n]: the array sorted in numerical order
Constraints
1 <= n <= 2 * 10^5
Each string is guaranteed to represent a positive integer without leading zeros.
The total number of digits across all strings in unsorted is between 1 and 10^6 (inclusive).
"""
def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted

if __name__ == '__main__':
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    result = bigSorting(unsorted)
    print('\n'.join(result))
    print('\n')