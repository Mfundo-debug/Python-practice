"""
Watson gives Sherlock an array of integers. Given the endpoints of an integer range, for all M in the range, find the minimum value of max(abs(M-A[i])) where A[i] is an element in the array.
Oce that has been determined for all integers in the ranger, return M which generated the maximum of those values. if there are multiple M that result in that value, return the smallest one.

Function Description:
Complete the sherlockAndMinimax function in the editor below. It should return an integer as described.

sherlockAndMinimax has the following parameters:
- arr: an array of integers
- p: an integer that represents the lowest value of the range for M
- q: an integer that represents the highest value of the range for M
Constraints
 1 <= n <= 100
    1 <= arr[i] <= 10^9
    1 <= p <= q <= 10^9
"""
def sherlockAndMinimax(arr, p, q):
    arr.sort()
    n = len(arr)
    max_diff = 0
    result = 0
    for i in range(n):
        if arr[i] >= p and arr[i] <= q:
            if i == 0:
                diff = abs(arr[i] - p)
            elif i == n - 1:
                diff = abs(arr[i] - q)
            else:
                diff = min(abs(arr[i] - arr[i - 1]) // 2, abs(arr[i] - arr[i + 1]) // 2)
            if diff > max_diff:
                max_diff = diff
                result = arr[i]
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    result = sherlockAndMinimax(arr, p, q)
    print(str(result) + '\n')