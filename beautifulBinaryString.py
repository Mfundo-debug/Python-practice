"""
Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring "010".
In one step, Alice can change a 0 to a 1 or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.
Example
b = 010
She can change any one element and have a beautiful string.
Function Description

Complete the beautifulBinaryString function in the editor below.

beautifulBinaryString has the following parameter(s):

string b: a string of binary digits
Returns

int: the minimum moves required
Constraints
1 ≤ |b| ≤ 100
b[i] ∈ {0, 1}
"""
def beautifulBinaryString(b):
    count = 0
    i = 0
    while i < len(b)-2:
        if b[i:i+3] == '010':
            count += 1
            i += 3
        else:
            i += 1
    print(count)
    return count
if __name__ =='__main__':
    n = int(input())
    b = input()
    result = beautifulBinaryString(b)