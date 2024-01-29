"""
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.
Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
"""
def advanced_sort(lst):
    return [[i]*lst.count(i) for i in set(lst)]

if __name__=='__main__':
    print(advanced_sort([2, 1, 2, 1]))
    print(advanced_sort([5, 4, 5, 5, 4, 3]))
    print(advanced_sort(["b", "a", "b", "a", "c"]))
    print(advanced_sort([]))