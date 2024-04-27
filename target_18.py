"""
Target = 18
[2,7,5,11,15]
Find the pair of numbers that sum up to the target
"""

def find_pair(arr, target):
    # Create a dictionary to store the difference and the index
    diff_dict = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in diff_dict:
            return (diff_dict[diff], i)
        diff_dict[arr[i]] = i
    return None

if __name__ == "__main__":
    arr = [2,7,5,11,15]
    target = 18
    print(find_pair(arr, target)) # (1, 3) -> 7 + 11 = 18