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
    def __init__(self, start, end=None, parent=None):
        self.start = start
        self.end = end
        self.parent = parent
        self.children = {}

class ActivePoint:
    def __init__(self, node, edge, length):
        self.node = node
        self.edge = edge
        self.length = length

def build_suffix_tree(s):
    root = Node(-1, -1)
    root.children[s[0]] = Node(0, len(s), root)
    active = ActivePoint(root, None, 0)
    remainder = 0
    for i in range(1, len(s)):
        remainder += 1
        while remainder > 0:
            if active.length == 0:
                if s[i] in active.node.children:
                    active.edge = s[i]
                    active.length += 1
                    break
                else:
                    active.node.children[s[i]] = Node(i, len(s), active.node)
                    remainder -= 1
            else:
                edge_start = active.node.children[active.edge].start
                if active.length < i - edge_start:
                    if s[edge_start + active.length] in active.node.children[active.edge].children:
                        active.node = active.node.children[active.edge]
                        active.edge = s[edge_start + active.length]
                        active.length = 1
                        break
                    else:
                        old_node = active.node.children[active.edge]
                        new_node = Node(old_node.start, old_node.start + active.length, active.node)
                        new_node.children[s[i]] = Node(i, len(s), new_node)
                        new_node.children[s[old_node.start + active.length]] = old_node
                        old_node.start += active.length
                        old_node.parent = new_node
                        active.node.children[active.edge] = new_node
                        remainder -= 1
                elif active.length == i - edge_start:
                    active.node = active.node.children[active.edge]
                    active.edge = None
                    active.length = 0
                else:
                    if s[edge_start + active.length] == s[i]:
                        active.length += 1
                        break
                    else:
                        old_node = active.node.children[active.edge]
                        new_node = Node(old_node.start, old_node.start + active.length, active.node)
                        new_node.children[s[i]] = Node(i, len(s), new_node)
                        new_node.children[s[old_node.start + active.length]] = old_node
                        old_node.start += active.length
                        old_node.parent = new_node
                        active.node.children[active.edge] = new_node
                        remainder -= 1
            if active.node != root:
                active.node = active.node.parent
            else:
                active.length -= 1
                if active.length > 0:
                    active.edge = s[i - remainder + 1]
    return root

def buildString(a, b, s):
    n = len(s)
    root = build_suffix_tree(s + "$")
    cost = [0]*(n+1)
    for i in range(1, n+1):
        cost[i] = cost[i-1] + a
        node = root
        j = i
        while j < n and s[j] in node.children:
            node = node.children[s[j]]
            edge_length = min(node.end, n+1) - node.start
            if i + edge_length <= n:
                cost[i+edge_length] = min(cost[i+edge_length], cost[i-1] + b)
            j += edge_length
    return cost[n]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,a,b = map(int,input().split())
        s = input()
        print(buildString(a,b,s))