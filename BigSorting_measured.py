import time

def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted

if __name__ == '__main__':
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    
    start_time = time.time()
    result = bigSorting(unsorted)
    end_time = time.time()
    
    print('\n'.join(result))
    print('\n')
    print("Execution time: ", end_time - start_time, "seconds")