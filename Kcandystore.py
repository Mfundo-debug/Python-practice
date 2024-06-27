"""
Jim enters a candy shop which has N different types of candies, each candy is of the same price. Jim has enough moeny to buy K candies.
In how many different ways can he purchase K candies if there are infinite candies of each kind?
Constraints
1 <= T <= 200
1 <= N <= 1000
1 <= K <= 1000
"""

def candy_store(n, k):
    return n**k

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(candy_store(n, k))