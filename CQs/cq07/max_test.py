from CQs.cq07.find_max import find_and_remove_max

"""Unit tests for find_and_remove_max function."""

__author__ = "730807192"


def test_expected_value() -> None:
    """Test for expected/typical values."""
    my_list: list[int] = [1, 2, 3, 4]
    my_num: int = find_and_remove_max(my_list)
    assert my_num == 4


def test_mutation() -> None:
    """Test for table mutation."""
    my_list: list[int] = [1, 2, 3, 4, 4]  # test for double entries
    expected_list: list[int] = [1, 2, 3]
    find_and_remove_max(my_list)
    assert my_list == expected_list


def test_unconventional() -> None:
    """Test for unconventional value (empty list)."""
    my_list: list[int] = []
    my_num: int = find_and_remove_max(my_list)
    assert my_num == -1  # -1 == empty list
