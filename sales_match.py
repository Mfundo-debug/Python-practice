"""
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example
n = 7
 ar = [1,2,1,2,1,3,2]

There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
Input Format

The first line contains an integer n, the number of socks represented in .
The second line contains  space-separated integers, ar[i], the colors of the socks in the pile.

Constraints
1 <= n <= 100
1 <= ar[i] <= 100 where 0 <= i < n
"""
def sockMerchant(n,ar):
    # Write your code here
    # n = number of socks
    # ar = array of socks
    # ar[i] = color of sock
    # return number of pairs
    # create a dictionary to store the color of the sock and the number of socks
    # create a variable to store the number of pairs
    # loop through the array of socks
    # if the color of the sock is not in the dictionary, add it and set the value to 1
    # if the color of the sock is in the dictionary, increment the value by 1
    # loop through the dictionary
    # if the value is greater than 1, divide it by 2 and add it to the number of pairs
    # return the number of pairs
    sock_dict = {}
    pairs = 0
    for sock in ar:
        if sock not in sock_dict:
            sock_dict[sock] = 1
        else:
            sock_dict[sock] += 1
    for sock in sock_dict:
        if sock_dict[sock] > 1:
            pairs += sock_dict[sock] // 2
    return pairs
if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n,ar)
    print(result)