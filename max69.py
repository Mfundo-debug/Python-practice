"""
Given a list of 9996969 numbers, iterate through the list and print the number if it is greater than 69.
"""
def max69(arr):
    for i in arr:
        if i > 69:
            print(i)
        else:
            continue

if __name__ == '__main__':
    arr = int(input("Enter the number of elements: "))
    arr = []
    for i in range(arr):
        arr.append(int(input("Enter the number: ")))
    max69(arr)
    

