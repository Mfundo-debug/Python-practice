"""
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate ofv2  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
Function Description

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2
Returns

string: either YES or NO
Input Format

A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.

Constraints
0 <= x1 < x2 <= 10000
1 <= v1 <= 10000
1 <= v2 <= 10000
"""
def kangaroo(x1,v1,x2,v2):
    if v1 > v2:
        if (x2-x1)%(v1-v2) == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    x1,v1,x2,v2 = map(int,input().split())
    print(kangaroo(x1,v1,x2,v2))