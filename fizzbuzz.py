"""
Given  a number n for each integer i in the ranger from 1 to n inclusive print one value per line a follows:
* if i is a multiple of both 3 and 5 print FizzBuzz
* if i is a multiple of 3 but not 5 print Fizz
* if i is a multiple of 5 but not 3 print Buzz
* if i is not multiple of 3 or 5 print the value of i
"""
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
        elif i % 3 == 0: print("Fizz")
        elif i % 5 == 0: print("Buzz")
        else: print(i)
if __name__ == '__main__':
    n = int(input().strip())
    fizzbuzz(n)