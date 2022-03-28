"""Exercise 8 Data Utils."""


__author__ = "730392257"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read data file as csv instead of strings
    csv_reader = DictReader(file_handle)
    # Read each row of CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close file when done
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce list[str of all values in single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], numbered: int) -> dict[str, list[str]]:
    """Produces table with only first numbered rows of data for each column."""
    result: dict[str, list[str]] = {}
 
    for column in table:
        first_numbered_values: list[str] = []
        i: int = 0
        while i < numbered:
            for item in table[column]:
                if i < numbered:
                    first_numbered_values.append(item)
                i += 1
        result[column] = first_numbered_values
        if numbered >= len(table[column]):
            return table
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces subset tables of original data."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = table[column]
    return result


def concat(a_table: dict[str, list[str]], b_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces new table combining two tables."""
    result: dict[str, list[str]] = {}
    for column in a_table:
        result[column] = a_table[column]
    for column in b_table:
        if column in result:
            result[column] += b_table[column]
        else:
            result[column] = b_table[column]
    return result


def count(frequency: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in input list."""
    result: dict[str, int] = {}
    for item in frequency:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def values(amount: dict[str, int]) -> str:
    """Counts how many high compared to low values appear in input list."""
    high_value: int = 0
    low_value: int = 0
    for item in amount:
        if item >= '6':
            high_value += amount[item]
        elif item <= '2':
            low_value += amount[item]
    result: str = f"high_value: {high_value}; low_value: {low_value}"
    return result
    
