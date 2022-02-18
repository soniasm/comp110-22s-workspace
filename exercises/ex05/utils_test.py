"""Test functions for exercise 05."""

__author__ = "730392257"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

# Test cases for function only_evens


def test_only_evens_empty() -> None:
    """Edge case: Tests for empty list in only_evens function."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_odd_number() -> None:
    """Use case: Tests if only one odd number is in the list."""
    xs: list[int] = [3]
    assert only_evens(xs) == []


def test_only_evens_multiple_numbers() -> None:
    """Use case: Tests when there are multiple numbers in list."""
    xs: list[int] = [2, 3, 4, 6, 9, 12, 15]
    assert only_evens(xs) == [2, 4, 6, 12]


# Test cases for sub function


def test_sub_end() -> None:
    """Edge case: Tests when start and end value are equal."""
    a_list: list[int] = [2, 4, 6, 8]
    start: int = 3
    end: int = 3
    assert sub(a_list, start, end) == []


def test_sub_single_number() -> None:
    """Use case: Tests when there is single number in list."""
    a_list: list[int] = [2]
    start: int = 0
    end: int = 1
    assert sub(a_list, start, end) == [2]


def test_sub_multiple_numbers() -> None:
    """Use case: Tests when multiple numbers are in list and start and end are far apart."""
    a_list: list[int] = [7, 13, 21, 18, 35]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [13, 21, 18]


# Tests for concat function


def test_concat_empty() -> None:
    """Edge case: Tests when there are no items in the lists."""
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []


def test_concat_single_number() -> None:
    """Use case: Tests when there is one item in each list."""
    a_list: list[int] = [1]
    b_list: list[int] = [2]
    assert concat(a_list, b_list) == [1, 2]


def test_concat_multiple_numbers() -> None:
    """Use case: Tests when there is multiple items in each list."""
    a_list: list[int] = [1, 2, 3, 4]
    b_list: list[int] = [5, 6, 7, 8]
    assert concat(a_list, b_list) == [1, 2, 3, 4, 5, 6, 7, 8]