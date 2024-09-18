"""CQ03 -- while loops."""

__author__ = "730807192"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0  # index of phrase
    count: int = 0  # count of the character
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1  # lol forgot to put this at first... whoops
    return count
