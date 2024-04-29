"""
Using Michael's algorithm to calculate the similarity between two strings.
list_1 =['apple', 'banana', 'cherry']
list_2 = ['pineapple', 'banana', 'cherry']
"""
import sys
from collections import defaultdict

def micalg(list_1, list_2):
    # Create a dictionary to store the frequency of each word in the two lists.
    freq = defaultdict(int)
    for word in list_1:
        freq[word] += 1
    for word in list_2:
        freq[word] += 1

    # Calculate the dot product of the two lists.
    dot_product = 0
    for word in freq:
        dot_product += freq[word] * freq[word]

    # Calculate the magnitude of the two lists.
    magnitude_1 = 0
    magnitude_2 = 0
    for word in list_1:
        magnitude_1 += freq[word] * freq[word]
    for word in list_2:
        magnitude_2 += freq[word] * freq[word]

    # Calculate the similarity between the two lists.
    similarity = dot_product / (magnitude_1 * magnitude_2) ** 0.5
    return similarity

if __name__ == "__main__":
    list_1 = ['apple', 'banana', 'cherry']
    list_2 = ['pineapple', 'banana', 'cherry']
    print(micalg(list_1, list_2))