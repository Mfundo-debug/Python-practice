"""
Given a sorted array (arr) and a number (V), can you print the index location of V in the array?
Example
arr = [1,2,3]
V = 3
Return 2 for a zero-based index array.
Function Description

Complete the introTutorial function in the editor below. It must return an integer representing the zero-based index of V.

introTutorial has the following parameter(s):

int arr[n]: a sorted array of integers
int V: an integer to search for
Returns

int: the index of V in arr
Constraints
1 <= n <= 1000
-1000 <= V <= 1000, V is an element of arr
It is guaranteed that V will occur in arr exactly once.
"""
def introTutorial(V, arr):
    # Write your code here
    for i in range(len(arr)):
        if arr[i] == V:
            return i
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    fptr.write(str(result) + '\n')
    fptr.close()