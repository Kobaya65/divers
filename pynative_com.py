"""From https://pynative.com/python-exercises-with-solutions/
"""
def exercise_1(phrase: str) -> str:
    """Reverse each word of a phrase.
    Args:
        phrase (str): phrase to be reversed
    Returns:
        str: Reverse phrase
    """
    mots = phrase.split()
    results = []
    result = ""

    results = [mot[::-1] for mot in mots]

    result = " ".join(results)

    return result


def exercise_3(number_list: list[int]) -> list[int]:
    """Remove items from a list while iterating.
        In this question, you need to remove items from a list during iteration without creating a separate copy of the list.
        Remove numbers greater than 50.
    Args:
        number_list (list[int]): liste of numbers to be processed
    Returns:
        list[int]: processed list of numbers
    """
    return [nombre for nombre in number_list if nombre <= 50]


if __name__ == "__main__":
    print(exercise_3([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
