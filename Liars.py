"""
You have N soldiers numbered from 1 to N. Each of your soldiers is either a liar or a truthful person. You have M sets of information about them.
Each set of information tells you the number of liars among a certain range of your soldiers. Let L be the total number of your liar soldiers.
 Since you can't find the exact value of L, you want to find the minimum and maximum value of L.
 Input Format
The first line contains two integers N and M, the number of soldiers and the number of sets of information.
Each of the next M lines contains three integers:
ABC where the set of soldiers numbered as {A, A+1, A+2, ..., B}, exactly C  of them are liars.
(1 ≤ Ai ≤ Bi <= n) and (0 ≤ Ci ≤ Bi - Ai)
Note: N and M are not more than 101, and it is guaranteed the given infroamtion is satisfiable.
Output Format
Print two integers, the minimum and maximum value of L.

Constraints:
1 ≤ N, M ≤ 100
0 ≤ C ≤ B - A
"""

def get(n, limit):
    edges = []
    virtual = n + 1
    for x in range(n):
        edges.append((x + 1, x, 0))
        edges.append((x, x + 1, 1))
    for x in range(n+1):
        edges.append((virtual, x, 0))
    for a, b, c in limit:
        edges.append((a - 1, b, c))
        edges.append((b, a - 1, -c))
    dist = [10 ** 10] * (n + 2)
    dist[virtual] = 0
    for x in range(n + 1):
        for a, b, c in edges:
            dist[b] = min(dist[b], dist[a] + c)
    return dist[n] - dist[0]

def liars(n, sets):
    rev = [[a, b, b - a + 1 - c] for [a, b, c] in sets]
    return get(n, sets), n - get(n, rev)

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    sets = []
    for _ in range(m):
        sets.append(list(map(int, input().rstrip().split())))
    result = liars(n, sets)
    print(result[0], result[1])
