"""
An integer d is a divisor of an integer n if the remainder of n/d=0 .

Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer.
Example
 n = 124
Check whether 1,2 and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.
n =111
Check whether 1,1 and 1 are divisors of 111. All 3 numbers divide evenly into 111 so return 3.
n =10
Check whether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.
Function Description

Complete the findDigits function in the editor below.

findDigits has the following parameter(s):

int n: the value to analyze
Returns

int: the number of digits in  that are divisors of 
Input Format
The first line is an integer, t, the number of test cases.
The t subsequent lines each contain an integer, n.

Constraints
1<=t<=15
0<n<10^9
"""
def findDigits(n):
    count=0
    for i in str(n):
        if int(i)!=0 and n%int(i)==0:
            count+=1
    return count
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        print(result)