"""Dictionary Exercise."""

__author__ = "730392257"


def invert(a_dictionary: dict[str, str]) -> dict:
    final_dictionary: dict[str, str] = {}
    for key in a_dictionary:
        value = a_dictionary[key]
        for item in final_dictionary:
            if item == value:
                raise KeyError("KeyError")
        final_dictionary[value] = key
    return final_dictionary


def favorite_color(b_dictionary: dict[str, str]) -> str:
    colors: dict[str, int] = {}
    for item in b_dictionary:
        color_string = b_dictionary[item]
        if color_string in colors:
            colors[color_string] += 1
        else: 
            colors[color_string] = 1
    frequent_value: int = 0
    frequent_key: str = ''
    for key in colors:
        if frequent_value == 0 or frequent_value < colors[key]:
            frequent_value = colors[key]
            frequent_key = str(key)
    return frequent_key


def count(a_list: list[str]) -> dict:
    final: dict[str, int] = {}
    for item in a_list:
        if item in final:
            final[item] += 1
        else:
            final[item] = 1
    return final