"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set([1,3,4]) is a strict superset of set([1,3]).
Set([1,3,4]) is not a strict superset of set([1,3,4]).
Set([1,3,4]) is not a strict superset of set([1,3,5]).

Input Format

The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.

Constraints
0 < len(set(A)) < 501
0 < N < 21
0 < len(otherSets) < 101
"""
from itertools import combinations

def strict_superset():
    set_a = set(map(int, input().split()))
    n = int(input())
    other_sets = [set(map(int, input().split())) for _ in range(n)]
    print(all([set_a.issuperset(other_set) for other_set in other_sets]))

def strict_superset_2():
    set_a = set(map(int, input().split()))
    print(all([set_a.issuperset(set(map(int, input().split()))) for _ in range(int(input()))]))

if __name__ == '__main__':
    strict_superset()
    # strict_superset_2()