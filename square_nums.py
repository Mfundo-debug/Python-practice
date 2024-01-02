def square_numbers(nums):
    squared_nums = [x**2 for x in nums]
    return squared_nums

def validate_input(user_input):
    numbers = user_input.split(",")
    cleaned_numbers = []
    for num in numbers:
        cleaned_num = num.strip()
        if cleaned_num.isdigit():
            cleaned_numbers.append(int(cleaned_num))
        else:
            raise ValueError("Invalid input. Please enter a valid list of numbers.")
    return cleaned_numbers

def main():
    try:
        user_input = input("Enter a list of integers (separated by commas): ")
        numbers = validate_input(user_input)
        result = square_numbers(numbers)
        print(result,"\n", "Sum of the squared numbers:", sum(result))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
