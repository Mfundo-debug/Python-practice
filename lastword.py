"""
Find the length of the last word
Example
hello world
the length of the last word from that sentence is 5.
"""
def lastWord(s):
    return len(s.split()[-1])

if __name__ == '__main__':
    s = input("Enter a sentence: ")
    print("The length of the last word is", lastWord(s))
    