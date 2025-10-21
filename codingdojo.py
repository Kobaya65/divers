"""Exercises from https://codingdojo.org."""

def diamond(letter: str) -> str:
    """Build a diamond with letters.
    From https://codingdojo.org/kata/Diamond/

    Args:
        letter (str): chosen letter
    Returns:
        str: the diamond as a string
    """
    def make_row(rang: int, ligne: int) -> str:
        """Build a row.

        Args:
            rang (int): rank of the letter in the alphabet
            ligne (int): index of the row
        Returns:
            str: the row with the given letter, which is deduced from the line number
        """
        return f"{" " * (rang - ligne - 1)}{chr(ligne + 65)}{" " * (ligne + ligne - 1)}{chr(ligne + 65)}\n"

    def make_a_row(rang: int) -> str:
        """Build the "A" row.

        Returns:
            str: the "A" row
        """
        return f"{" " * rang}A\n"

    letter = letter.upper()
    if letter == "A":
        return "A"

    rang = ord(letter) - 64
    bottom_row = rang - 2
    solution = ""

    solution += make_a_row(rang - 1)
    # top of the diamond
    for ligne in range(1, rang):
        solution += make_row(rang=rang, ligne=ligne)
    # bottom of the diamond
    for ligne in range(bottom_row, 0, -1):
        solution += make_row(rang=rang, ligne=ligne)
    solution += make_a_row(rang - 1)

    return solution


if __name__ == "__main__":
    print(diamond("k"))
