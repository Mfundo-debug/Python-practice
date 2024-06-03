"""
Sansa has an array. She wants to find the value obtained by XOR in the contiguous subarrays, followed by XOR in the values obtained.

Function Description

Complete the sansaXor function in the editor below.

sansaXor has the following parameter(s):
int arr[n]: an array of integers
Returns

int: the result of calculations
Constraints:
1 <= t <= 5
1 <= n <= 10^5
1 <= arr[i] <= 10^8
"""
def sansaXor(arr):
    if len(arr) % 2 == 0:
        return 0
    result = 0
    for i in range(0, len(arr), 2):
        result ^= arr[i]
    return result
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = sansaXor(arr)
        print(result)