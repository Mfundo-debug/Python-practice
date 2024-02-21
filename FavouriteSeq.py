"""
Johnny, like every mathematician, has his favorite sequence of distinct natural numbers. Let’s call this sequence M.
Johnny was very bored, so he wrote dwon N copies of the sequence M in his big Notebook.
One day, when Johnny was out, his little sister Mary erased some numbers(possibly zero) from every copy of the sequence M and then threw the notebook out onto the street.
Can you reconstruct the sequence?
In the inpute there are N sequences of natural numbers representing the N copies of the sequence M in the notebook. In each of them all numbers are distinct.
your task is to construct the shortest sequence S that might have been the original sequence M.. if are many such sequences, you should find the lexicographically smallest one.
Note
Sequence A[1...n] is lexico graphically smaller than sequence B[1...n] if there is such an index i (1<=i<=n) that A[i]<B[i] and A[j]=B[j] for each j(1<=j<i)
COnstrainsts
1 <= N <= 10^3
2 <= K <= 10^3
All values in the input are distinct and are between 1 and 10^3
"""
from collections import deque, defaultdict

def favouriteSeq(N, arr):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for seq in arr:
        for i in range(len(seq) - 1):
            graph[seq[i]].append(seq[i+1])
            indegree[seq[i+1]] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result

if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    result = favouriteSeq(N, arr)
    print(" ".join(map(str, result)))