"""Recurrsion practice with nodes."""

from __future__ import annotations  # Not for now, lol

__author__ = "730807192"


class Node:
    """Recurssive node class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """New node object with value and next set."""
        self.value = val
        self.next = next


def value_at(head: Node | None, index: int) -> int:
    """Determines the value at the index of the linked list."""
    if head:
        if index == 0:
            # Reached needed index
            return head.value
        else:
            # Next node, decrease index
            return value_at(head.next, index - 1)
    else:
        # Index != to len of linked list
        raise IndexError("Index is out of bounds on the list.")


def max(head: Node | None) -> int:
    """Determines the max value present in the linked list."""
    if head:
        if not (head.next is None):
            # Prevents head from being none.. but why is it allowed in the parameters?
            val: int = max(head.next)
            if val > head.value:
                # Loops through all the vals, get the greatest
                return val
        return head.value
    else:
        raise ValueError("Cannot call max with None")


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list from a list using nodes."""
    if len(items) > 0:
        # Uses python slice // [1:]
        # Creates new node, rather than modifing
        return Node(items[0], linkify(items[1:]))
    return None


def scale(head: Node | None, factor: int) -> Node | None:
    """Creates a scaled linked list using nodes."""
    if head:
        # Don't modify the original, rather create a new node link
        return Node(head.value * factor, scale(head.next, factor))
    return None


def to_str(head: Node | None) -> str:
    """Converts a node linked list to a string."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)  # loops through adding every member of the list
        return f"{head.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
