"""
You are given two arrays, A and B, both containing N integers.
A pair of indices (i,j) is beautiful if the ith element of array A is equal to the jth element of array B.
In other words, pair (i,j) is beautiful if and only if A[i] = B[j].
A set containing beautiful pairs is called a beautiful set.
A beautiful set is called pairwise disjoint if for every pair (i,j) belonging to the set there is no repetition of either l[i] or r[j] values.
For example, if A = [10, 11, 12, 5, 14] and B = [8,9,11,11,5], the beautiful set [(1,2), (1,3), (3,4)] is  not pairwise disjoint as there is a repetition of 1, that l[0][0] = l[1][0].
Your task is to change exactly 1 element in B so that the size of the pairwise disjoint beautiful set is maximum.

Function Description

Complete the beautifulPairs function in the editor below. It should return an integer that represents the maximum number of pairwise disjoint beautiful pairs that can be formed.

beautifulPairs has the following parameters:

A: an array of integers
B: an array of integers

Constraints
1 <= n <= 10^3
1 <= A[i], B[i] <= 10^3
"""
def beautifulPairs(A,B):
    count = 0
    for i in range(len(A)):
        if A[i] in B:
            B.remove(A[i])
            count += 1
    if count == len(A):
        return count - 1
    return count + 1

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    print(beautifulPairs(A,B))