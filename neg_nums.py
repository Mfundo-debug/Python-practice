def find_negative_numbers():
    x = input("Enter a list of numbers: ")
    x = [int(num) for num in x.split()]
    neg_nums = [num for num in x if num < 0]
    return neg_nums

if __name__ == "__main__":
    neg_nums = find_negative_numbers()
    print(neg_nums)
