"""Test for Dictionary Exercise."""

__author__ = "730392257"


from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    a_dictionary: dict[str, str] = {}
    assert invert(a_dictionary) == {}


def test_invert_one_key() -> None:
    a_dictionary: dict[str, str] = {'banana': 'fruit'}
    assert invert(a_dictionary) == {'fruit': 'banana'}


def test_invert_multiple_keys() -> None:
    a_dictionary: dict[str, str] = {'banana': 'fruit', 'carrot': 'vegetable', 'coffee': 'drink'}
    assert invert(a_dictionary) == {'fruit': 'banana', 'vegetable': 'carrot', 'drink': 'coffee'}


def test_favorite_color_empty() -> None:
    b_dictionary: dict[str, str] = {}
    assert favorite_color(b_dictionary) == ''


def test_favorite_color_one_highest() -> None:
    b_dictionary: dict[str, str] = {'Andrew': 'blue', 'Will': 'blue', 'Alyssa': 'yellow', 'Stuti': 'blue'}
    assert favorite_color(b_dictionary) == 'blue'


def test_favorite_color_two_highest() -> None:
    b_dictionary: dict[str, str] = {'Andrew': 'blue', 'Will': 'blue', 'Alyssa': 'yellow', 'Stuti': 'yellow', 'Ethan': 'green'}
    assert favorite_color(b_dictionary) == 'blue'

    
def test_count_empty() -> None:
    a_list: list[str] = []
    assert count(a_list) == {}


def test_count_one_item() -> None:
    a_list: list[str] = ['banana']
    assert count(a_list) == {'banana': 1}


def test_count_multiple_items() -> None:
    a_list: list[str] = ['banana', 'pear', 'apple', 'banana', 'banana']
    assert count(a_list) == {'banana': 3, 'pear': 1, 'apple': 1}