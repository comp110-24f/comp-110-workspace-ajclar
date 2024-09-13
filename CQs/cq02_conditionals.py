"""Fun guess the number game! :)"""

__author__ = "730807192"


def guess_a_number() -> None:
    """Guess the number terminal game!"""
    secret: int = 7
    x: str = input("Guess a number: ")  # Allows user input
    number_x: int = int(x)  # Converts X so it can be compared
    print("Your guess was " + x)
    if int(number_x) == secret:
        print("You got it!")
    elif int(number_x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(number_x) > secret:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
