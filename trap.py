"""
Create a user registration form that traps the user in a loop until they enter a valid email address.
"""
import re
import sys

def main():
    while True:
        email = input("Enter your email address: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Thank you for registering!")
            break
        else:
            print("Invalid email address. Please try again.")

if __name__ == "__main__":
    sys.exit(main())