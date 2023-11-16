"""
atson likes to challenge Sherlock's math ability.
He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints.
Sherlock must determine the number of square integers within that range.

Note: A square integer is an integer which is the square of an integer, e.g.1,4,9,16,25.
Example
a= 24
b= 49
There are three square integers in the range: 25,36 and 49. Return 3.
Function Description

Complete the squares function in the editor below. It should return an integer representing the number of square integers in the inclusive range from  to .

squares has the following parameter(s):

int a: the lower range boundary
int b: the upper range boundary
Returns

int: the number of square integers in the range
Input Format

The first line contains q, the number of test cases.
Each of the next q lines contains two space-separated integers, a and b, the starting and ending integers in the ranges.
Constraints
1<=q<=100
1<=a<=b<=10^9
"""
import math
def squares(a,b):
    sqrt_a = math.ceil(math.sqrt(a))
    sqrt_b = math.floor(math.sqrt(b))
    return sqrt_b - sqrt_a + 1
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        print(result)