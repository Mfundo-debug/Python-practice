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
from collections import defaultdict

def favouriteSeq(N, arr):
    order = defaultdict(list)
    for i in range(N):
        for j in range(len(arr[i])):
            order[arr[i][j]].append(i)
    res = sorted(order.keys(), key=lambda x: order[x][0])
    return res

if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    result = favouriteSeq(N, arr)
    print(" ".join(map(str, result)))