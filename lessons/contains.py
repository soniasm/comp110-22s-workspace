"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))
# Define a function named contains
# Two parameters:
#   1. needle - the string we are searching for
#   2. haystack - the list we are searching through


def contains(needle: str, haystack: list[str]) -> bool:
    #  Algorithm:
    #   For each item in the haystack
    #       test if it is equal to the needle
    #           If so, return True
    for item in haystack:
        if item == needle:
            return True
#   After testing all items, return False because not found
#  Returnes true if needle in haystaack, false otherwise
    return False


if __name__ == "__main__":
    main()