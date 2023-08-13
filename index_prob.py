"""
You are given a list of N lowercase English letters. 
For a given integer K, you can select any K indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format

The input consists of three lines. The first line contains the integer N, denoting the length of the list. 
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints
1 <= N <= 10
1 <= K <= N
"""
def prob(n, k):
    return 1 - (1 - (1/n))**k
if __name__ == '__main__':
    n = int(input())
    s = input().split()
    k = int(input())
    print(prob(n, k))