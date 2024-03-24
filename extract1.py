"""
Given a list of words extract only those words that are of length 5 or more from a list of words.
and they must be only consonants.
"""

def extractConsonants(words):
    consonants = 'aeiouAEIOU'
    return [word for word in words if all(letter in consonants for letter in word)]


if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange', 'pear', 'plum', 'strawberry', 'watermelon']
    print(extractConsonants(words))