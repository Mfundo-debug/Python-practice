"""
given a word, return the letter that is repeated first
Example:
    "hello" -> "l"
    "mississippi" -> "i"
    "abcde" -> None
    "Guarantteed" -> "a"
    "letter" -> "t"
"""
def repeatedletter(word):
    # for letter in word:
    #     if word.count(letter) > 1:
    #         return letter
    # return None
    for i in range(len(word)):
        if word[i] in word[i+1:]:
            return word[i]
    return None

if __name__ == '__main__':
    word = input().strip()
    print(repeatedletter(word))
