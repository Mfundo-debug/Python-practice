"""
FUnction called SearchingChallenge(strArr) In the strArr parameter containing key:value pairs where the key is a string and the value is an integer.
Your program should return a string with new key:value pairs separated by a comma such that each key appears only once with the total values summed up.
For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] then your program should return the string A:6,B:2.
Your final output string should return the keys in alphabetical order.
Exclude keys that have a value of 0 after being summed up.
"""
def SearchingChallenge(strArr):
    # Dictionaary to store the sum of values for each key
    key_values = {}
    # Process each key:value pair
    for pair in strArr:
        key, value = pair.split(':')
        key_values[key] = key_values.get(key, 0) + int(value)

    # Filter keys with non-zero values and sort them alphabetically
    result = sorted([f"{key}:{value}" for key, value in key_values.items() if value != 0])

    # Return the result as a comma-separated string
    return ','.join(result)
if __name__ == '__main__':
    # keep this function call here
    print(SearchingChallenge(input()))

#Comment
"""
A step-by-step explanation of the code:
The function `SearchingChallenge` takes a string `strArr` as an argument. This string is expected to contain a list of key:value pairs, separated by a comma. 
For example: `"B:-1,A:1,B:3,A:5"`.
The first line inside the function splits `strArr` into a list of strings at the `,` character using `strArr.split(',')`. Each of these strings represents a key:value pair.
The `for` loop iterates over each key:value pair in the list. The `split()` method is used to split each pair at the `:` character, resulting in a list of two strings: `key` and `value`.
The `key_values` dictionary is used to store the sum of values for each key. The `get()` method is used to retrieve the current value for the key, or 0 if the key is not present in the dictionary.
The `sorted()` function is used to sort the list of key:value pairs alphabetically. The `items()` method is used to get a list of key:value pairs from the dictionary.
The `if` statement is used to filter out key:value pairs with a value of 0.
The `join()` method is used to join the list of key:value pairs into a single string, separated by commas.
The `if __name__ == '__main__':` block is used to test the function. If the script is run directly (not imported as a module), then `__name__` will be `'__main__'`, and the code inside this block will be executed.

for the time complexity, it's O(n), where n is the total number of key:value pairs in the input string. This is because each key:value pair is processed once when splitting the string, and once when adding the value to the dictionary.

The time complexity of this function is O(n log n), where n is the number of key-value pairs in strArr. This is because each pair is processed once (O(n)), and then the keys are sorted (O(n log n)). The space complexity is O(n), as a dictionary is used to store the sum of values for each key.
"""