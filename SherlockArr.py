"""
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.
Example
arr = [5,6,8,11]
8 is between two subarrays that sum to 11
arr = [1]
Function Description

Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):

int arr[n]: an array of integers
Returns

string: either YES or NO
Constraints
1 <= T <= 10
1 <= n <= 10^5
1 <= arr[i] <= 2 * 10^4
0 <= i < n
"""
def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    for num in arr:
        if left_sum == total_sum - left_sum - num:
            return 'YES'
        left_sum += num
    return 'NO'

if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)