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

if __name__ == "__main__":
    entiers_multiples()
