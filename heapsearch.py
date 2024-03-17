"""
implementation of heapsearch algorithm
 any list
"""
import heapq

def heap_search(lst, item):
    heapq.heapify(lst)
    while lst:
        if lst[0] == item:
            return True
        heapq.heappop(lst)
    return False

if __name__ == "__main__":
    lst = [3, 2, 5, 1, 4]
    print(heap_search(lst, 3))  #
    print(heap_search(lst, 6))  