"""Wordle ripoff! :)"""

__author__ = "730807192"


def input_guess(char_count: int) -> str:
    """Validates and returns an inputed guess."""
    correct_length: bool = False
    guess: str = input(f"Enter a {char_count} character word: ")
    while not (correct_length):
        # ^ Could you do "while (True)" since you're returning when it's valid anyways?
        if len(guess) == char_count:
            correct_length = True
            return guess
        else:
            guess = input(f"That wasn't {char_count} chars! Try again: ")
    return ""  # Shouldn't be needed? but the autograded requests it


def contains_char(word: str, character: str) -> bool:
    """Returns whether word contains any instances of character."""
    assert len(character) == 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == character:
            return True
        idx += 1
    return False


# Below are the emoji unicodes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, word: str) -> str:
    """Returns an = len emoji sequnce as guess/word based on letter occupancy."""
    assert len(guess) == len(word)
    toReturn: str = ""
    idx: int = 0
    while idx < len(word):
        if contains_char(word, guess[idx]):
            if word[idx] == guess[idx]:
                toReturn += GREEN_BOX  # Correct letter location
            else:
                toReturn += YELLOW_BOX  # Letter is in word; incorrect location
        else:
            toReturn += WHITE_BOX  # Letter is not in word
        idx += 1  # Forget this :( ... as per usual haha
    return toReturn


def main(word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    guessed_correctly = False
    while (turn_count <= 6) and not (guessed_correctly):
        # ^ Turn count hasn't passed, and hasn't guess correctly already
        # Also, turn count should be <= to include 6/6 turns vs 5/6 :)
        print(f"=== Turn {turn_count}/6 ===")
        guess: str = input_guess(len(word))
        print(emojified(guess, word))
        if guess == word:
            guessed_correctly = True
        else:
            turn_count += 1
    if guessed_correctly:
        print(f"You won in {turn_count}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("codes")
