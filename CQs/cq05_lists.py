"""Mutating functions."""

__author__ = "730807192"


def manual_append(toMutate: list[int], toAdd: int) -> None:
    # Basically useless, but shows how toMutuate works in memory.
    toMutate.append(toAdd)


def double(toDouble: list[int]) -> None:
    """Loops through every index of the list to duplicate it's value."""
    index: int = 0
    while index < len(toDouble):
        toDouble[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # Same id in memory

double(list_2)
print(list_1)
print(list_2)
