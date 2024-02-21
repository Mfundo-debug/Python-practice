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

n = int(input())
before_maps = defaultdict(set)
after_maps = defaultdict(set)
for _ in range(n):
    k = int(input())
    sequence = map(int, input().split())
    prev = 0
    for num in sequence:
        if prev:
            before_maps[num].add(prev)
        after_maps[prev].add(num)
        prev = num

m = []
actives = set(active for active in after_maps[0] if not before_maps[active])
while actives:
    next_step = sorted(actives)[0]

    actives.remove(next_step)
    for step in after_maps[next_step]:
        before_maps[step].remove(next_step)

    actives.update(active for active in after_maps[next_step] if not before_maps[active])
    m.append(next_step)

print(' '.join(map(str, m)))