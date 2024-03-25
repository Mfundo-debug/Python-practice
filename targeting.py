"""
Given an array [2,7,5,11]
find the targets that sum 9
"""

def find_target(arr, target):
    # create a dictionary to store the values
    d = {}
    for i in range(len(arr)):
        # check if the target - arr[i] is in the dictionary
        if target - arr[i] in d:
            return [d[target - arr[i]], i]
        # store the value in the dictionary
        d[arr[i]] = i
    return None

if __name__ == '__main__':
    arr = [2,7,5,11]
    target = 9
    print(find_target(arr, target)) # [0, 2]