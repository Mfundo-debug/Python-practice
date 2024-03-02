"""
A gene is reprsented as a string of length n (where n is divisible by 4), composed of the letters A, C, T, and G. It is considered to be steady if each of the four letters occurs exactly n/4 times. For example, GACT and AAGTGCCT are both steady genes.
Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string gene. It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of gene and replace it with any string of the same length.
Modifying a large substring of bear genes can be dangerous. Given a string gene, can you help Limak find the length of the smallest possible substring that he can replace to make gene a steady gene?
Note: A substring of a string s is a subsequence made up of zero or more continous characters of s.
As an example, consider gene = ACTGAAAG. The substring AA just before or after G can be trplsced either CT or TC. One selection would create ACTGACTG.
Function Description

Complete the steadyGene function in the editor below. It should return an integer that represents the length of the smallest substring to replace.

steadyGene has the following parameter:

gene: a string

Constraints
4 <= n <= 500000
n is divisible by 4
gene[i] is the element of [CGAT]
subtask
4 <= n <= 2000 in tests worth 30% of the total score.
failed 1 test
"""
def steadyGene(gene):
    n = len(gene)
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in gene:
        count[char] += 1
    start = 0
    end = 0
    min_len = n
    while end < n:
        count[gene[end]] -= 1
        end += 1
        while all(val <= n/4 for val in count.values()):
            min_len = min(min_len, end - start)
            count[gene[start]] += 1
            start += 1
    return min_len

if __name__ == '__main__':
    n = int(input().strip())
    gene = input()
    result = steadyGene(gene)
    print(result)