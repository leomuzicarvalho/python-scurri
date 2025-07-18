from typing import List, Union


def three_five_sequence(start: int = 1, end: int = 100) -> List[Union[int, str]]:
    """Generate three-five sequence."""
    result: List[Union[int, str]] = []
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("ThreeFive")
        elif i % 3 == 0:
            result.append("Three")
        elif i % 5 == 0:
            result.append("Five")
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    result = three_five_sequence()
    for item in result:
        print(item) 