"""Combines two strings together."""

__author__ = "730807192"


def concat(str1: str, str2: str) -> str:
    """Returns the combination of two strings."""
    return str1 + str2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
