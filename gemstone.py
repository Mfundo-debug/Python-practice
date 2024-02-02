"""
There is a collection of rocks where each rock has various minerals embeded in it.
 Each type of mineral is designated by a lowercase letter in the range ascii[a-z].
There may be multiple occurrences of a mineral in a rock. 
A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.
Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.
Example
arr = ["abc","abc","bc"]
The minerals b and c appear in each rock, so there are 2 gemstones.
Function Description

Complete the gemstones function in the editor below.

gemstones has the following parameter(s):

string arr[n]: an array of strings
Returns

int: the number of gemstones found
Constraints
1 <= n <= 100
1 <= |arr[i]| <= 100
Each composition arr[i] consists of only lower-case Latin letters ('a'-'z').
"""

def gemstones(arr):
    # Write your code here
    gemstones = 0
    for mineral in arr[0]:
        is_gemstone = True
        for rock in arr[1:]:
            if mineral not in rock:
                is_gemstone = False
                break
        if is_gemstone:
            gemstones += 1
    return gemstones

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)