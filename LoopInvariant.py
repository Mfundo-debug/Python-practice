"""
Loop Invariant
Challenge

In the InsertionSort code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted.
Constraints
1 <= Size <= 1000
-1500 <= V <= 1500, V ∈ arr
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    print(*arr)

if __name__ == '__main__':
    s = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort(arr)