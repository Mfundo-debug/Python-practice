"""
Given a list of integers, return the sum of all the integers that are positive and even.
If there are no positive and even integers, return 0.
Example:
Input: [1, 2, 3, 4, 5]
Output: 6
"""
def sum_positive_even_numbers(numbers):
    # Initialize the sum
    sum = 0
    # Loop through the numbers
    for number in numbers:
        # Check if the number is positive and even
        if number > 0 and number % 2 == 0:
            # Add the number to the sum
            sum += number
    return sum

if __name__ == '__main__':
    # Test the function with the example input
    numbers = [1, 2, 3, 4, 5]
    result = sum_positive_even_numbers(numbers)
    print(result)  # Output: 6