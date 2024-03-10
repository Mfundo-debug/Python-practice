"""
Arrays exercise part 3 using numpy
calculate eugenetic distance between two populations
calculate the average of the genetic distance between two populations
"""
import numpy as np

def genetic_distance(pop1, pop2):
    """
    Calculate the genetic distance between two populations
    """
    return np.sum(pop1 != pop2) / len(pop1)

def average_genetic_distance(pop1, pop2):
    """
    Calculate the average genetic distance between two populations
    """
    return np.mean(np.sum(pop1 != pop2) / len(pop1))

if __name__ == '__main__':
    pop1 = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
    pop2 = np.array([1, 0, 1, 0, 0, 1, 0, 1, 0, 0])
    print(genetic_distance(pop1, pop2))
    print(average_genetic_distance(pop1, pop2))