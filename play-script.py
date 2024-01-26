"""
Write a script that plays the game of Hangman.
using list comprehension to find the index of the letter in the word
"""
def hangman(word):
    wrong = 0
    stages = ["",
              "_________          ",
              "|                  ",
              "|         |        ",
              "|         0        ",
              "|        /|\       ",
              "|        / \       ",
              "|                  "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = [i for i, x in enumerate(rletters) if x == char]
            for i in cind:
                board[i] = char
            rletters[cind[0]] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

if __name__ == '__main__':
    word = input("Enter a word: ")
    hangman(word)