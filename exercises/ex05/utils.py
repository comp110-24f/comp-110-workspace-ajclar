"""List utility functions."""

__author__ = "730807192"


def only_evens(old_list: list[int]) -> list[int]:
    """Returns a list with only the even values of the orginal list."""
    new_list: list[int] = []
    for value in old_list:
        if value % 2 == 0:
            # if even, add to end of new_list
            new_list.append(value)
    return new_list


def sub(old_list: list[int], index: int, stop: int) -> list[int]:
    """Returns a list with only the values contained from index to stop."""
    new_list: list[int] = []
    if index < 0:
        index = 0
    if stop > len(old_list):
        stop = len(old_list)  # < means stop NOT stop-1; therefore, len() vs len()-1
    if (len(old_list) == 0) or (index >= len(old_list)) or (stop <= 0):
        return new_list
    while index < stop:  # < means stop NOT stop-1
        # for indexes between start/stop, add to the new_list
        new_list.append(old_list[index])
        index += 1
    return new_list


def add_at_index(my_list: list[int], value: int, at_index: int) -> None:
    """Inserts a new value at a specified index."""
    if (at_index < 0) or (at_index > len(my_list)):
        raise IndexError("Index is out of bounds for the input list")
    my_list.append(value)  # Adds the value to the end of the list
    index: int = len(my_list) - 1
    while index > at_index:
        # Then swaps the current indexed value with the previous
        # util the value is at the desired index
        current_value: int = my_list[index]
        my_list[index] = my_list[index - 1]
        my_list[index - 1] = current_value
        index -= 1
