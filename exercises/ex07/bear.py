"""File to define Bear class."""

__author__ = "730807192"


class Bear:
    """Biggie (hungry) bear class."""

    # Didn't know you had to docstring classes lol

    age: int
    hunger_score: int

    def __init__(self):
        """Initalizes a bear with age 0 and hunger 0."""
        self.age = 0
        self.hunger_score = 0

    def eat(self, num_fish: int) -> None:
        """Increases hunger health by number of fish eaten."""
        self.hunger_score += num_fish

    def one_day(self) -> None:
        """Increases age by 1 and hunger by -1."""
        self.age += 1
        self.hunger_score -= 1
