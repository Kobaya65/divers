"""From https://python.developpez.com/exercices/?page=Objets#Un-point-dans-le-plan.
"""
from math import sqrt

class point_plan(object):
    """This class allows you to store the coordinates of a point,
    and also to calculate the distance to this point from another coordinate.
    """
    def __init__(self, x: float, y: float) -> None:
        self.x_a = x
        self.y_a = y

    def __repr__(self) -> str:
        chaine = ""
        try:
            chaine = f"<x={self.x_a}, y={self.y_a}>"
        except Exception as e:
            print(e)

        return chaine

    def affiche_point(self) -> None:
        """Displays coordinates of the point.
        """
        print(self.__repr__())

    def calcul_distance(self, x: float, y: float) -> float:
        """Calculates distance between (x, y) and the original point.
        Args:
            x (float): x position
            y (float): y position
        Returns:
            float: distance between original point and coordinate passed as argument
        """
        result = 0
        try:
            result = sqrt((x - self.x_a) ** 2 + (y - self.y_a) ** 2)
        except Exception as e:
            print(e)

        return result


if __name__ == "__main__":
    point = point_plan(2, 2)
    print(f"Coordonnés d'origine : {point}")

    x_1 = 2
    y_1 = 4
    distance_1 = point.calcul_distance(x_1, y_1)
    print(f"Distance entre le point d'origine {point} et <x={x_1}, y={y_1}> : {distance_1}")

    x_2 = 8.45
    y_2 = -4.639
    distance_2 = point.calcul_distance(x_2, y_2)
    print(f"Distance entre le point d'origine {point} et <x={x_2}, y={y_2}> : {distance_2}")
