def square_numbers(nums):
    squared_nums = [x**2 for x in nums]
    return squared_nums

if __name__ == "__main__":
    try:
        user_input = input("Enter a list of numbers (separated by commas): ")
        numbers = [int(x) for x in user_input.split(",")]
        result = square_numbers(numbers)
        print(result,"\n",
             "sum of the squared numbers", sum(result) )
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")
