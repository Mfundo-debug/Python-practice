"""
Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

Design your counting sort to be stable.

Example
arr = [[0,'a'],[1,'b'],[0,'c'],[1,'d']]

Function Description

Complete the countSort function in the editor below. It should construct and print the sorted strings.

countSort has the following parameter(s):

string arr[n][2]: each arr[i] is comprised of two strings, x and s
Returns
- Print the finished array with each element separated by a single space.

Note: The first element of each arr[i], x , must be cast as an integer to perform the sort.

Input Format

The first line contains n, the number of integer/string pairs in the array arr.
Each of the next n contains x[i] and s[i], the integers (as strings) with their associated strings.

Constraints
1 <= n <= 1000000
n is even
1 <= |s| <= 10
0 <= x < 100, x ∈ arr
s[i] consists of characters in the range ascii[a-z]
"""
def countSort(arr):
    
