"""
Jim is doing his discrete maths homework which requires him to repeatedly calculate nCr(n choose r) for different values of n. Knowing that this is time consuming, he goes to his sister June for help. June, being a computer science student knows how to convert this into a computer program and generate the answers quickly. She tells him, by storing the lower values of nCr(n choose r), one can calculate the higher values using a very simple formula.

If you are June, how will you calculate nCr values for different values of n?
Since nCr values can be very large, output them modulo 10^9.

Output format:
For each n output the list of nC0 to nCn each separated by a single space in a new line. if the number is large, output it modulo 10^9.

Constraints:
 1 <= n <= 1000
 1 <= T <=200
"""
def solve(n):
    MOD = 10**9 + 7
    nCr = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                nCr[i][j] = 1
            else:
                nCr[i][j] = (nCr[i-1][j-1] + nCr[i-1][j]) % MOD
    return nCr

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        nCr = solve(n)
        result = []
        for i in range(n+1):
            result.append(' '.join(map(str, nCr[i][:i+1])))
        results.append('\n'.join(result))
    
    print('\n\n'.join(results))