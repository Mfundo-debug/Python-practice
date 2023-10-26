"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to 10^-4 are acceptable.
Example
arr = [1, 1, 0, -1, -1]
There are n = 5 elements, two positive, two negative and one zero. 
Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000.
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Input Format

The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].

Constraints
0 < n <= 100
-100 <= arr[i] <= 100
"""
def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos/len(arr):.6f}")
    print(f"{neg/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)