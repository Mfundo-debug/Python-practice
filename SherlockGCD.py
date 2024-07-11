import math

"""
Sherlock is stuck while solving a problem: Given an array A = {a1, a2, a3, a4, ..., aN}. He wants to know if there exists a subset B of this array which follows the below conditions:
B is a non-empty subset.
There is no element common between any two elements of B.
Constraints
1 <= T <= 10
1 <= N <= 100
1 <= ai <= 10^5 for all (1 <= i <= N)

"""
def solve(a):
    if len(a) == 1:
        return "NO"
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if math.gcd(a[i], a[j]) == 1:
                return "YES"
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
