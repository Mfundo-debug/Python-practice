"""
Using Michael's algorithm to calculate the similarity between two strings.
list_1 =['apple', 'banana', 'cherry']
list_2 = ['pineapple', 'banana', 'cherry']
"""
from collections import defaultdict
import math

def micalg(list_1, list_2):
    # Create a dictionary to store the frequency of each word in the two lists.
    freq_1 = defaultdict(int)
    freq_2 = defaultdict(int)
    for word in list_1:
        freq_1[word] += 1
    for word in list_2:
        freq_2[word] += 1

    # Calculate the dot product of the two lists.
    dot_product = sum(freq_1[word] * freq_2[word] for word in freq_1)

    # Calculate the magnitude of the two lists.
    magnitude_1 = math.sqrt(sum(freq_1[word]**2 for word in freq_1))
    magnitude_2 = math.sqrt(sum(freq_2[word]**2 for word in freq_2))

    # Calculate the similarity between the two lists.
    similarity = dot_product / (magnitude_1 * magnitude_2)
    return similarity

if __name__ == "__main__":
    list_1 = ['apple', 'banana', 'cherry']
    list_2 = ['pineapple', 'banana', 'cherry']
    print(micalg(list_1, list_2))