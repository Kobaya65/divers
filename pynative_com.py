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


def name_and_age(name: str, age : int) -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-1-create-a-function-in-python
    exercise 1
    """
    print(f"Your name is {name} and you are {age} years old.")

def variable_length_of_arguments(*args) -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-2-create-a-function-in-python-with-variable-length-arguments
    exercise 2
    """
    for value in args:
        print(value)

def return_multiple_values_from_a_function(a: int, b: int) -> tuple[int, int]:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-3-create-a-function-in-python-that-returns-multiple-values
    exercise 3
    """
    return (a + b, a * b)

def show_employee(name: str, salary: int = 9000) -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-4-create-a-function-in-python-with-default-arguments
    exercise 4
    """
    print(f"Employee Name: {name}, Salary: {salary}")
    
def outer_function(a: int, b: int) -> int:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-5-create-an-inner-function-in-python
    exercise 5
    """
    def inner_function(a: int, b: int) -> int:
        """Addition of a and b.

        Args:
            a (int): first argument
            b (int): second ergument

        Returns:
            int: sum of the arguments
        """
        return a + b

    return inner_function(a, b) + 5

def sum_of_numbers(number: int) -> int:
    """https://pynative.com/python-recursion-exercise-with-solutions/#h-exercise-1-write-a-recursive-function-to-calculate-the-sum-of-numbers-from-0-to-10
    exercise 1
    """
    if number <= 1:
        return number
    else:
        return number + sum_of_numbers(number - 1)


if __name__ == "__main__":
    print(sum_of_numbers(57))
