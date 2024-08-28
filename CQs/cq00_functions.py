"""CQ00 Function Exercise"""

__author__ = "730807192"


def main() -> None:
    """Controls the program & prints the mimic result"""
    print(mimic(message=input("What is your message?")))


def mimic(message: str) -> str:
    """Returns the same string you gave it"""
    return message


if __name__ == "__main__":
    main()
