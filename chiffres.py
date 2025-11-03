"""Python exercices from various web sites.
"""
def entiers_multiples() -> None:
    """Les entiers naturels inférieurs à 10 multiples de 3 ou de 5 sont 3,5,6 et 9. Leur somme est égale à 23.
    Trouver la somme des entiers inférieurs à 1000 et multiples de 3 ou 5.
    https://python.dellasantina.corsica/defis/project-euler/1-10/exercices
    """
    result = 0
    for chiffre in range(1, 1000):
        if (chiffre % 3 == 0) or (chiffre % 5 == 0):
            result += chiffre

    print(result)


def number_to_lcd(number: int) -> str:
    """Displays a number like on a lcd screen.
    From https://codingdojo.org/kata/NumberToLCD.
     _     _  _     _  _  _  _  _ 
    | |  | _| _||_||_ |_   ||_||_|
    |_|  ||_  _|  | _||_|  ||_| _|

    Args:
        number (int): number to be displayed

    Returns:
        str: string
    """
    # each key of the dictionary corresponds to a line of the lcd display
    chiffres = {
        0: {
            0: " _ ",
            1: "   ",
            2: " _ ",
            3: " _ ",
            4: "   ",
            5: " _ ",
            6: " _ ",
            7: " _ ",
            8: " _ ",
            9: " _ ",
        },
        1: {
            0: "| |",
            1: "  |",
            2: " _|",
            3: " _|",
            4: "|_|",
            5: "|_ ",
            6: "|_ ",
            7: "  |",
            8: "|_|",
            9: "|_|",
        },
        2: {
            0: "|_|",
            1: "  |",
            2: "|_ ",
            3: " _|",
            4: "  |",
            5: " _|",
            6: "|_|",
            7: "  |",
            8: "|_|",
            9: " _|",
        },
    }    

    result = ""
    number_str = str(number)
    for niv in range(3):
        for x in number_str:
            result += chiffres[niv][int(x)]
        result += "\n"

    return result


if __name__ == "__main__":
    print(number_to_lcd(1234567890))
