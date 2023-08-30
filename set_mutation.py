"""
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.
Constraints:
0 < len(set(A)) < 1000
0 < len(otherSets) < 100
0 < N < 100
"""
def set_mutation():
    # Get the number of elements in set A
    n = int(input())
    # Get the elements in set A
    a = set(map(int, input().split()))
    # Get the number of other sets
    n_other_sets = int(input())
    # Iterate through the number of other sets
    for i in range(n_other_sets):
        # Get the operation name and the length of the other set
        operation_name, len_other_set = input().split()
        # Get the other set
        other_set = set(map(int, input().split()))
        # Perform the operation
        if operation_name == 'intersection_update':
            a.intersection_update(other_set)
        elif operation_name == 'update':
            a.update(other_set)
        elif operation_name == 'symmetric_difference_update':
            a.symmetric_difference_update(other_set)
        elif operation_name == 'difference_update':
            a.difference_update(other_set)
    # Print the sum of elements in set A
    print(sum(a))

if __name__ == '__main__':
    set_mutation() 