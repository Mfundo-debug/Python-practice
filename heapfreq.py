"""
Given an array ([2,4,2,5,6,3,2])
use heap algorithm to find the frequency of a number in an unsorted array.

"""
import heapq

def heap_search(arr, target):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    count = 0
    while heap:
        num = heapq.heappop(heap)
        if num == target:
            count += 1
    return count

if __name__=='__main__':
    arr = [2,4,2,5,6,3,2]
    target = 2
    count = heap_search(arr, target)
    print(f'The frequency of {target} is {count}')