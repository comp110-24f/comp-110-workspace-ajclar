"""Finds and returns the max value of a list -- also removes it."""

__author__ = "730807192"


def find_and_remove_max(my_list: list[int]) -> int:
    """Finds and returns the max value of a list -- also removes it."""
    if len(my_list) == 0:
        return -1  # -1 if list is empty
    else:
        largest: int = my_list[0]
        for num in my_list:
            if num > largest:
                largest = num
        index: int = 0
        while index < len(my_list):
            if my_list[index] == largest:
                my_list.pop(index)  # pop to remove index
            else:
                index += 1  # only increase index if index isn't removed
        return largest
