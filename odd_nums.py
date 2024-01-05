# Get user input for the range of numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Validate the input
if start >= end:
    print("Invalid input. The starting number should be less than the ending number.")
else:
    # Generate the list of odd numbers
    x = list(range(start, end+1))
    odd_nums = [num for num in x if num % 2 != 0]
    print(odd_nums)
