"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases,T .
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Constraints
0 < T < 21
0 < Number of elements in each set < 1001
"""

def setAB():
    T = int(input())
    for i in range(T):
        nA = int(input())
        A = set(map(int, input().split()))
        nB = int(input())
        B = set(map(int, input().split()))
        print(A.issubset(B))
if __name__ == '__main__':
    setAB()