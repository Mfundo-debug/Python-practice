"""
A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers,
you have the same value you started with.
Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2 x d digits long or (2 x d) -1  digits long.
Split the string representation of the square into two parts,l  and r. The right hand part, r must be d digits long. The left is the remaining substring. 
Convert those two substrings back to integers, add them and see if you get n.
Example
n =5 
d =1
Function Description

Complete the kaprekarNumbers function in the editor below.

kaprekarNumbers has the following parameter(s):

int p: the lower limit
int q: the upper limit
Constraints
0 < p < q < 100000
"""
def kaprekarNumbers(p,q):
    kaprekar = []
    for i in range(p,q+1):
        if i == 1:
            kaprekar.append(i)
        else:
            square = i*i
            square = str(square)
            d = len(str(i))
            if len(square) == 2*d:
                l = square[:d]
                r = square[d:]
                if l != '' and r != '' and int(l) + int(r) == i:
                    kaprekar.append(i)
            elif len(square) == 2*d - 1:
                l = square[:d-1]
                r = square[d-1:]
                if l != '' and r != '' and int(l) + int(r) == i:
                    kaprekar.append(i)
    if len(kaprekar) == 0:
        print("INVALID RANGE")
    else:
        print(*kaprekar)

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p,q)
