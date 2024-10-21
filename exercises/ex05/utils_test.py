from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Tests for the list utility functions."""

__author__ = "730807192"


# only_evens


def test_only_evens_edge() -> None:
    """Tests the empty list edge case of the only_evens function."""
    my_list: list[int] = []
    should_return: list[int] = []
    did_return = only_evens(my_list)
    assert did_return == should_return


def test_only_evens_return() -> None:
    """Tests whether a correct list is returned by the only_evens function."""
    my_list: list[int] = [1, 2, 3, 4, 5]
    should_return: list[int] = [2, 4]
    did_return = only_evens(my_list)
    assert did_return == should_return


def test_only_evens_mutate() -> None:
    """Tests whether the orginal list is mutated or not."""
    my_list: list[int] = [1, 2, 3, 4, 5]
    did_return = only_evens(my_list)
    assert not (my_list == did_return)


# sub


def test_sub_edge_small() -> None:
    """Tests the smaller end edge case of the sub function."""
    my_list: list[int] = [1, 2, 3, 4]
    should_return: list[int] = [1, 2]
    did_return = sub(my_list, -1, 2)
    assert did_return == should_return


# below & above -- worth having both when I was struggling


def test_sub_edge_large() -> None:
    """Tests the larger end edge case of the sub function."""
    my_list: list[int] = [1, 2, 3, 4]
    should_return: list[int] = [3, 4]
    did_return = sub(my_list, 2, 4)
    assert did_return == should_return


def test_sub_return() -> None:
    """Tests whether a correct list is returned by the sub function."""
    my_list: list[int] = [1, 2, 3, 4, 5]
    should_return: list[int] = [2, 3]
    did_return = sub(my_list, 1, 3)
    assert did_return == should_return


def test_sub_mutate() -> None:
    """Tests whether the orginal list is mutated or not."""
    my_list: list[int] = [1, 2, 3, 4, 5]
    did_return = sub(my_list, 1, 2)
    assert not (my_list == did_return)


# add_at_index


def test_add_at_index_edge() -> None:
    """Tests the empty list edge case of the add_at_index function."""
    my_list: list[int] = []
    add_at_index(my_list, 1, 0)
    assert my_list[0] == 1


def test_add_at_index_return() -> None:
    """Tests whether a valued is correct based on the add_at_index function."""
    my_list: list[int] = [1, 2, 3, 5]
    add_at_index(my_list, 4, 3)
    assert my_list[4] == 3


def test_add_at_index_mutate() -> None:
    """Tests whether the orginal list is mutated or not."""
    my_list: list[int] = [1, 2, 3, 5]
    should_become: list[int] = [1, 2, 3, 4, 5]
    add_at_index(my_list, 4, 3)
    assert my_list == should_become


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    my_list: list[int] = [1, 2, 3]
    # pytest used as indexerror is not the same as an incorrect return/mutate
    with pytest.raises(IndexError):
        add_at_index(my_list, 4, 5)
