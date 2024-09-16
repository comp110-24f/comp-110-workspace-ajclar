"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730807192"


def input_word() -> str:
    chosen_word: str = input("Enter a 5-character word: ")
    if len(chosen_word) != 5:
        print("Error: Word must contain 5 characters")
        exit()  # Exit when there's an error, before returning /any/ value
    return chosen_word


def input_letter() -> str:
    chosen_letter: str = input("Enter a single character: ")
    if len(chosen_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return chosen_letter


def contains_char(word: str, letter: str) -> None:
    found_count: int = 0
    print("Searching for " + letter + " in " + word)

    # a loop would be so wonderful here
    if word[0] == letter:
        print(letter + " found at index 0")
        found_count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        found_count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        found_count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        found_count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        found_count += 1

    if found_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif found_count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(found_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # HAVE! to remember to do para=arg


if __name__ == "__main__":
    main()
