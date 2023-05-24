def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    print((" ".join(board)))
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
            print((" ".join(board)))
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "_" not in board:
            print("YOU WIN!")
            print("".join(board))
            win = True
            break
    if not win:
        print(print("\n".join(stages[0:wrong])))
        print(f"You lose. The word was {word}.")

hangman("bangs")