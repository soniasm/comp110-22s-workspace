"""Ex 05 function skeletons and implementations."""

__author__ = "730392257"


# Name: only_evans
# Arguments: A list of integers.
def only_evens(xs: list[int]) -> list:
    """Returns only even elements in a list of integers."""
    i: int = 0
    even: list[int] = []
    # Returns: A list of integers, containing only the even elements of the input parameter
    while i < len(xs):
        if xs[i] % 2 == 0:
            even.append(xs[i])
        i += 1
    return even

# Name: sub
# Parameters: A list and two ints, where the first int serves as a start index and the second int serves as an end index(not inclusive)
# Returns: A list which is a subset of the given list between the specified start index and the end index - 1.


def sub(a_list: list[int], start: int, end: int) -> list:
    """Returns subset of list between start and end index."""
    subset: list[int] = []
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return []
    else:
        while start <= end - 1:
            subset.append(a_list[start])
            start += 1
        return subset

# Name: concat
# Parameters: Two lists of ints
# Returns: A list containing all the elements of the first list followed by all elements of the second list.


def concat(a_list: list[int], b_list: list[int]) -> list:
    """Returns list of values in the two parameter lists."""
    all: list[int] = []
    i: int = 0
    while i < len(a_list):
        all.append(a_list[i])
        i += 1
    i = 0
    while i < len(b_list):
        all.append(b_list[i])
        i += 1
    return all