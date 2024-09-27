"""Combines two strings into coordinates."""

__author__ = "730807192"


def get_coords(xs: str, ys: str) -> None:
    """Prints the grid coords of two strings."""
    idx1: int = 0
    while idx1 < len(xs):
        idx2: int = 0
        # I had this ^ under idx1, but it needs to be here to run more than once
        while idx2 < len(ys):
            print("(" + xs[idx1] + "," + ys[idx2] + ")")
            idx2 += 1
        idx1 += 1
