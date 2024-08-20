"""
You are given 3 numbers a,b, and x. You need to output the multiple of x which is closest to a^b. If more than one answer is possible then output the smallest one.

Constraints:
 1 <= a,b,x <= 10^9
 1 <= T <= 10^5
 1<= a^b <= 10^9
 
"""
def closestNumber(a,b,x):
    m = a**b
    n = m // x
    if abs(m - n * x) < abs(m - (n + 1) * x):
        return n * x
    else:
        return (n + 1) * x
    
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        a,b,x = map(int, input().rstrip().split())
        result = closestNumber(a,b,x)
        print(str(result) + '\n')