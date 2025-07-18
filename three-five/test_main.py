import pytest
from main import three_five_sequence, print_three_five
from typing import Union


def test_three_five_sequence() -> None:
    result = three_five_sequence(1, 15)
    expected: list[Union[int, str]] = [1, 2, "Three", 4, "Five", "Three", 7, 8, "Three", "Five", 11, "Three", 13, 14, "ThreeFive"]
    assert result == expected


def test_print_three_five(capsys: pytest.CaptureFixture[str]) -> None:
    print_three_five(1, 5)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\nThree\n4\nFive\n" 