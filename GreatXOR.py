"""
Given a long integer x, count the number of values of a satisfying the following conditions:
- a xor x > x
- 0 < a < x
where a and x are long integers and xor is the bitwise XOR operator.
you are given q queries, and each query is in the form of a long integer denoting x.
For each query, print the total number of values of a satisfying the conditions above on a new line.
For example, you are given the value x = 5. Condition 2 requires that a < x The following tests are run:
1 xor 5 = 4
2 xor 5 = 7
3 xor 5 = 6
4 xor 5 = 1
The only values that satisfy the conditions are 2 and 3. This gives us the result 2.

Function Description

Complete the theGreatXor function in the editor below. It should return an integer that represents the number of values satisfying the constraints.

theGreatXor has the following parameter(s):

x: an integer

Constraints
1 <= q <= 10^5
1 <= x <= 10^10
Subtasks
For 50% of the maximum score:
1 <= q <= 10^3
1 <= x <= 10^4
"""

def theGreatXor(x):
    # Find the binary representation of x
    binary = bin(x)[2:]
    # Count the number of 0s in the binary representation of x
    count = binary.count('0')
    # Return 2 raised to the power of the number of 0s in the binary representation of x
    return 2**count

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        x = int(input().strip())
        result = theGreatXor(x)
        print(result)