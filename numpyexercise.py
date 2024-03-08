"""
Today we play with numpy library, by creating a function, that computes:
1. The mean of the elements of a list
2. The standard deviation of the elements of a list
3. The variance of the elements of a list
4. The median of the elements of a list
5. The maximum value of the elements of a list
6. The minimum value of the elements of a list
7. The sum of the elements of a list
8. The product of the elements of a list
"""
def compute_statistics(list):
    import numpy as np
    mean = np.mean(list)
    std = np.std(list)
    var = np.var(list)
    median = np.median(list)
    max = np.max(list)
    min = np.min(list)
    sum = np.sum(list)
    prod = np.prod(list)
    return mean, std, var, median, max, min, sum, prod

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    print(compute_statistics(list))