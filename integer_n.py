"""given an integer n, perform the following conditional actions:
    - if n is odd, print Weird
    - if n is even and in the inclusive range of 2 to 5, print Not Weird
    - if n is even and in the inclusive range of 6 to 20, print Weird
    - if n is even and greater than 20, print Not Weird"""
n = int(input("Enter a number: "))
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
else:
    print("Invalid input")

# alternative solution: using list comprehension
# word = ["Weird" if n % 2 != 0 else "Not Weird"\
#          if n % 2 == 0 and n in range(2, 6) else "Weird"\
#               if n % 2 == 0 and n in range(6, 21) else "Not Weird" \ 
#               if n % 2 == 0 and n > 20 else "Invalid input"\
#                   for n in [int(input("Enter a number: "))]]
    