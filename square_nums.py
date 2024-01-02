def square_numbers(nums):
    squared_nums = [x**2 for x in nums]
    return squared_nums

if __name__ == "__main__":
    user_input = input("Enter a list of numbers (separated by commas): ")
    numbers = [int(x) for x in user_input.split(",")]
    result = square_numbers(numbers)
    print(result)
