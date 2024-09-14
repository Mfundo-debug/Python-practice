"""
Adam is standing at the point (a, b) in an infinite 2D grid. He wants to know if he can reach the point (x, y) or not. 
The only operation he can do is to move to the point (a+b, b) or (a, a+b) from some point (a, b). 
It is given that he can move to any point on this 2D grid, i.e., the points having positive or negative (a+b) and (b) co-ordinates.
Tell Adam whether he can reach (x, y) or not.

Constraints:

1 <= T <= 100
1 <= a, b, x, y <= 10^18
"""

def solve(a, b, x, y):
    
    if a > x or b > y:
        return False
    if a == x and b == y:
        return True
    return solve(a+b, b, x, y) or solve(a, a+b, x, y)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, x, y = map(int, input().split())
        print("YES" if solve(a, b, x, y) else "NO")

        