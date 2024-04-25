"""
The Absolute difference is the positive difference between two values a and b,
is written |a-b| or |b-a| and they are equal. If a =3 and b=2, |3-2| = |2-3| = 1.
Given an array of integers, find the minimum absolute difference between any two elements in the array.
Example
arr = [-2, 2, 4]
There are 3 pairs of numbers: [-2, 2], [-2, 4], [2, 4]. The absolute differences for these pairs are:
|(-2)-2| = 4, |(-2)-4| = 6, |2-4| = 2. The minimum absolute difference is 2.

Function Description
Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

int arr[n]: an array of integers
Returns

int: the minimum absolute difference found

Constraints
2 ≤ n ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9
"""
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)