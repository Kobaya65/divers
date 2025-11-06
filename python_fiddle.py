"""Various python challenges from python-fiddle.com
"""
def main() -> None:
    """https://python-fiddle.com/?checkpoint=1760713867
    """
    num_terms = 10
    fibonacci = [0, 1]

    while len(fibonacci) < num_terms:
        next_term = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_term)

    print(fibonacci)

def add(*args) -> float | int:
    """Adds an arbitrary number of arguments together and returns the sum.
    https://python-fiddle.com/challenges/add-args

    Args:
        *args: The input arguments
    Returns:
        int or float: The sum of all the arguments
    """
    somme = 0
    for arg in args:
        somme += arg

    return somme

def find_substring(strings: list[str], substring: str) -> bool:
    """Check if a substring is present in any string within a list.
    https://python-fiddle.com/challenges/check-substring-in-list

    Args:
        strings (list of str): The list of strings to search within
        substring (str): The substring to search for
    Returns:
        bool: True if the substring is found in any string, False otherwise
    """
    result = False
    for mot in strings:
        if substring in mot:
            result = True
            break

    return result

def ascii_value(char: str) -> int:
    """Returns the ASCII value of the given character.
    https://python-fiddle.com/challenges/ascii-value-of-character

    Args:
        char (str): A single character
    Returns:
        int: The ASCII value of the character
    """
    res = ord(char)

    return res

def capital_words_spaces(input_string: str) -> str:
    """Insert spaces between words starting with capital letters in the given string.
    Use a regular expression to identify the pattern and insert spaces.
    https://python-fiddle.com/challenges/add-spaces-between-capital-words

    Args:
        input_string (str): The input string containing words without spaces
    Returns:
        str: A new string with spaces inserted between capitalized words
    """
    import re

    pattern, res, pos = r"[A-Z]", "", 0
    for maj in re.finditer(pattern=pattern, string=input_string):
        # not to process first character if it is uppercase
        if maj.start():
            res += f"{input_string[pos:maj.start()]} "

        pos = maj.start()

    res += input_string[pos:]

    return res

def extract_column_from_csv(file_path: str, column_index: int) -> list[str]:
    """https://python-fiddle.com/challenges/csv-dict

    Args:
        file_path (str): The path to the CSV file
        column_index (int): The index of the column to extract (0-based)
    Returns:
        list of str: A list containing the values from the specified column
    """
    import csv
    import pandas as pd

    column_data = []
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > column_index:
                column_data.append(row[column_index])

    return column_data

def create_csv_file() -> None:
    """Create a csv file to be used in extract_column_from_csv().
    """
    import os.path
    import csv

    file_path = f"{os.path.expanduser("~")}/Documents/data.csv"
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        writer.writerow({"Name": "John", "Age": "25", "City": "New York"})
        writer.writerow({"Name": "Emma", "Age": "30", "City": "London"})

    del os.path
    del csv


if __name__ == "__main__":
    create_csv_file()
