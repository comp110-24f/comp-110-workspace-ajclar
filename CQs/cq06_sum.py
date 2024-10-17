"""Summing the elements of a list using different loops"""

__author__ = "730807192"


def w_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a while loop."""
    total: float = 0.0
    index: int = 0
    while index < len(vals):
        total += vals[index]
        index += 1  # >:(
    return total


def f_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a for loop."""
    total: float = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a for range loop."""
    total: float = 0.0
    for index in range(0, len(vals)):
        total += vals[index]  # index is.. well index, not the val
    return total


# TESTING:
# list_a: list[float] = [1.0, 2.0, 3.0]
# list_b: list[float] = []

# print(w_sum(list_a))
# print(w_sum(list_b))

# print(f_sum(list_a))
# print(f_sum(list_b))

# print(f_range_sum(list_a))
# print(f_range_sum(list_b))
