"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23. The path is denoted by numbers in bold.
    3
   7 4
  2 4 6
 8 5 9 3
That is, 3 + 7 + 4 + 9 =23 .
Find the maximum total from top to bottom of the triangle given in input.
Input Format
First line contains T, the number of testcases. For each testcase:
First line contains N, the number of rows in the triangle.
For next  lines, i'th line contains i numbers.
Constraints
1 <= T <= 10
1 <= N <= 15
All numbers between 0 and 100(inclusive)
"""
def max_path_sumI(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        triangle = []
        for i in range(N):
            triangle.append(list(map(int, input().split())))
        print(max_path_sumI(triangle))