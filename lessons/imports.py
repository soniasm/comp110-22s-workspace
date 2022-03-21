"""Examples of importing in Python."""


from lessons import helpers

# Alias a module / imported name as a another name
from lessons import helpers as hp

# Import names defined globally in a module
from lessons.helpers import powerful


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()