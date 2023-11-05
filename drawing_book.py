"""
Function Description

Complete the pageCount function in the editor below.

pageCount has the following parameter(s):

int n: the number of pages in the book
int p: the page number to turn to
Returns

int: the minimum number of pages to turn
Input Format

The first line contains an integer n, the number of pages in the book.
The second line contains an integer, p, the page to turn to.

Constraints
1 <= n <= 10^5
1 <= p <= n
"""

def pageCount(n,p):
    if n%2 == 0:
        n += 1
    if p%2 == 0:
        p += 1
    return min(p//2, (n-p)//2)

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n,p)
    print(result)