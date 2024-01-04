def get_user_input():
    while True:
        try:
            numbers = input("Enter a list of numbers: ")
            return [int(num) for num in numbers.split()]
        except ValueError:
            print("Invalid input. Please enter a list of numbers.")

def find_negative_numbers(numbers):
    return [num for num in numbers if num < 0]

if __name__ == "__main__":
    numbers = get_user_input()
    neg_nums = find_negative_numbers(numbers)
    print(neg_nums)