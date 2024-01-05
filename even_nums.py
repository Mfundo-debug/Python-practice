# Prompt the user to enter the numbers
nums = input("Enter a list of numbers (separated by commas): ")

# Split the input string into a list of numbers
nums_list = nums.split(",")

# Initialize an empty list to store even numbers
even_nums = []

# Iterate over each number in the list
for num in nums_list:
    # Perform input validation
    try:
        num = int(num)
        if num % 2 == 0:
            even_nums.append(num)
    except ValueError:
        print(f"Invalid input: {num} is not a valid number")

# Print the list of even numbers
print(even_nums)

# Alternative method using list comprehension
even_nums = [int(num) for num in nums_list if num.isdigit() and int(num) % 2 == 0]
print(even_nums)