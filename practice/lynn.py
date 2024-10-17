words: list[str] = []
all_guessed: bool = False

while not (all_guessed):
    if len(words) > 0:
        toPrint: str = "Remember: "
        for word in words:
            if not (word == words[len(words) - 1]):
                toPrint += word + ", "
            else:
                print(toPrint + "& " + word + "!")
    words = []
    for player_num in [1, 2, 3, 4]:
        guess: str = input(f"Player{player_num}, guess a word: ")
        words.append(guess)
    index: int = 0
    all_guessed = True
    while index < len(words):
        if not (words[0] == words[index]):
            all_guessed = False
        index += 1
    if not (all_guessed):
        print("Try again!\n\n")
    else:
        print("GOOD JOB!")
