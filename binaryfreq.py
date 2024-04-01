"""
arr = ([2,2,1,1,3,3])
Using binary search, find the frequency of a number in a sorted array.
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 3]
    target = 2
    idx = binary_search(arr, target)
    if idx == -1:
        print('Element not found')
    else:
        count = 1
        left, right = idx - 1, idx + 1
        while left >= 0 and arr[left] == target:
            count += 1
            left -= 1
        while right < len(arr) and arr[right] == target:
            count += 1
            right += 1
        print(f'The frequency of {target} is {count}')