"""File to define Fish class."""

__author__ = "730807192"


class Fish:
    """Fish class... swim, swim, swim!"""

    age: int

    def __init__(self):
        """Initalizes a fish with age of 0."""
        self.age = 0
        return None

    def one_day(self):
        """Increases the age of a fish by 1."""
        self.age += 1
        return None
