"""
Given a list of rational numbers,find their product.

Concept
The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value.
Say you have a list, say [1,2,3] and you have to find its sum.
Input Format

First line contains n, the number of rational numbers.
The ith of next n lines contain two integers each, the numerator( N_i ) and denominator( D_i ) of the ith rational number in the list.

Constraints
1 <= n <= 100
1 <= N_i,D_i <= 10^9
"""
from fractions import Fraction
from functools import reduce
def product(fracs):
    t = reduce(lambda x, y : x * y, fracs) 
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)