"""Replicating list functions."""

__author__ = "730807192"


def all(toCheck: list[int], num: int) -> bool:
    """Checks if every value in the list is equal to num."""
    index: int = 0
    if len(toCheck) == 0:
        # Return false if list is empty
        return False
    while index < len(toCheck):
        if not (toCheck[index] == num):
            # Cut the loop short if *any* value isn't the same.
            return False
        index += 1
    return True


def max(toCheck: list[int]) -> int:
    """Returns the greatest value contained in toCheck."""
    if len(toCheck) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    largest_num: int = toCheck[0]  # -math.huge?
    while index < len(toCheck):
        if largest_num < toCheck[index]:
            largest_num = toCheck[index]
        index += 1
    return largest_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines wether list_1 and list_2 have deep equality."""
    index: int = 0
    if not (len(list_1) == len(list_2)):
        return False  # False if they aren't even the same length
    while index < len(list_1):
        if not (list_1[index] == list_2[index]):
            return False
        index += 1  # Forgot this little pesk
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds the values contained within list_2 to the end of list_1."""
    index: int = 0
    while index < len(list_2):
        list_1.append(list_2[index])
        # I forgot 4 a sec that append exist & was going to loop through both lists haha
        index += 1  # ...yeah


if __name__ == "__main__":
    list_1: list[int] = [1, 2, 3]
    print(all(list_1, 1))
    print(all([1, 1, 1], 1))
    print(max(list_1))
    # print(max([])) works correctly
    print(is_equal(list_1, [4, 5, 6]))
    print(is_equal(list_1, list_1))
    print(is_equal(list_1, [1, 2, 3, 4]))
    extend(list_1, [4, 5, 6])
    print(list_1)
