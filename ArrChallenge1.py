"""
Read the array stored in strArr which will represent a list of comma-separated numbers sorted in ascending order.
the second list of comma-separated numbers represent a second list of ascending order numbers (also with no duplicates).
your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order.
if there is no intersection, return the string false.
"""
def ArrayChallenge(strArr):
    #split the input string into two arrays
    arr1, arr2 = [set(map(int, arr.split(','))) for arr in strArr.split('-')]
    #find the intersection of the two arrays
    common_elements = sorted(arr1.intersection(arr2))
    #if there are no common elements, return false
    if common_elements:
        return ','.join(map(str, common_elements))
    else:
        return 'false'
if __name__ == '__main__':
    # keep this function call here
    print(ArrayChallenge(input()))


#Comment
"""
for the time complexity, it's O(n), where n is the total number of elements in both lists.
 This is because each element is processed once when converting the strings to sets, and set intersection is also an O(n) operation. 
 The sorting operation is O(n log n), but since it's applied to the intersection of the two sets,
which is likely to be smaller than the original sets, the overall time complexity is dominated by the O(n) operations.
"""
