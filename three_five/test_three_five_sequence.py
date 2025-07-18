from main import three_five_sequence
from typing import Union


def test_three_five_sequence() -> None:
    result = three_five_sequence(1, 15)
    expected: list[Union[int, str]] = [1, 2, "Three", 4, "Five", "Three", 7, 8, "Three", "Five", 11, "Three", 13, 14, "ThreeFive"]
    assert result == expected 