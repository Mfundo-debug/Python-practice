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
A step-by-step explanation of the code:

1. The function `ArrayChallenge` takes a string `strArr` as an argument. This string is expected to contain two lists of numbers, separated by a `-`. For example: `"1,3,4,7,13-1,2,4,13,15"`.

2. The first line inside the function splits `strArr` into two separate strings at the `-` character using `strArr.split('-')`. Each of these strings represents a list of numbers.

3. The split strings are then converted into sets of integers. This is done by first splitting each string at the `,` character using `arr.split(',')` to get a list of strings. Then, `map(int, arr.split(','))` converts each string in the list to an integer.
 Finally, `set(map(int, arr.split(',')))` converts the list of integers to a set. This is done for both strings, resulting in two sets of integers: `arr1` and `arr2`.

4. The intersection of `arr1` and `arr2` is found using `arr1.intersection(arr2)`. This gives a set of integers that are present in both `arr1` and `arr2`.

5. The intersecting elements are sorted using `sorted()`, and then converted back into a string using `','.join(map(str, common_elements))`. This results in a string of numbers separated by commas.

6. If there are no common elements between `arr1` and `arr2`, `common_elements` will be an empty set. In this case, the function returns the string `'false'`.

7. The `if __name__ == '__main__':` block is used to test the function. If the script is run directly (not imported as a module), then `__name__` will be `'__main__'`, and the code inside this block will be executed. 
The `input()` function is used to read a string from the user, which is passed to the `ArrayChallenge` function. The result is then printed to the console.



for the time complexity, it's O(n), where n is the total number of elements in both lists.
 This is because each element is processed once when converting the strings to sets, and set intersection is also an O(n) operation. 
 The sorting operation is O(n log n), but since it's applied to the intersection of the two sets,
which is likely to be smaller than the original sets, the overall time complexity is dominated by the O(n) operations.
"""
