"""
Task
You are given an expression in a line. Read that line as a string variable, such as var, 
and print the result using eval(var)
Constraint
Input string is less than 100 characters.
Sample Input
print(2 + 3)
Sample Output
5
"""
def evaluate_string(string):
    try:
        return eval(string)
    except:
        return None

if __name__ == '__main__':
    string = input()
    result = evaluate_string(string)
    if result is not None:
        print(result)
