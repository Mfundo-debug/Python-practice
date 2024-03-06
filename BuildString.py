"""
Greg wants to build a string, S of length N. Starting with an empty string, he can perform any of the following operations:
1. Add a character to the end of S for A dollars.
2. Copy any substring of S and then add it to the end of S for B dollars.
Calculate minimum amount of money Greg needs to build the string S.
Input Format:
The first line contains the number of test cases, T.
The 2T subsequent lines describe the test cases. 
The first line contains the 3 space-separated integers N, A, and B.
The second line contains the string S.
Constraints
1 <= T <= 3
1 <= N <= 3*10^4
1 <= A, B <= 10000
"""
class Node:
    def __init__(self):
        self.child = [None]*26
        self.count = 0

def add(node, s, i):
    if i < len(s):
        if not node.child[ord(s[i])-ord('a')]:
            node.child[ord(s[i])-ord('a')] = Node()
        node.child[ord(s[i])-ord('a')].count += 1
        add(node.child[ord(s[i])-ord('a')], s, i+1)

def remove(node, s, i):
    if i < len(s):
        node.child[ord(s[i])-ord('a')].count -= 1
        remove(node.child[ord(s[i])-ord('a')], s, i+1)

def buildString(a, b, s):
    n = len(s)
    root = Node()
    add(root, s, 0)
    cost = a
    i = 1
    while i < n:
        temp = root
        j = i
        while j < n and temp.child[ord(s[j])-ord('a')] and temp.child[ord(s[j])-ord('a')].count > 0:
            temp = temp.child[ord(s[j])-ord('a')]
            j += 1
        if j-i > 1 and (j-i)*a > b:
            cost += b
            add(root, s, j)
        else:
            cost += a
            add(root, s, i)
        i = j
    return cost

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,a,b = map(int,input().split())
        s = input()
        print(buildString(a,b,s))