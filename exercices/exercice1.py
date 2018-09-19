# -*- coding: utf-8 -*-

"""exercice1.py

Consignes :
  Créer une calculette basique qui permettra de réaliser les opérations `+`, `-`, `/`, `*`.

  Le programme devra comporter au moins les 2 fonctions suivantes :
    - `ask_operation` qui demandera à l'utilisateur l'opération qu'il souhaite réaliser
    - `ask_number_value` qui demandera un nombre à l'utilisateur

  Tant que l'utilisateur ne souhaite pas quitter, le programme proposera de réaliser une opération.
  La gestion d'une mauvaise entrée utilisateur devra être traitée.

Usage :
  python exercice1.py

Code :
"""


def ask_operator():
    """
    Demande une opération à l'utilisateur

    :return: Opération
    :rtype: str
    """
    op_list = ['+', '-', '/', '*']
    op = ''
    while op not in op_list:
        op = input('Entrez une opération ( + | - | / | * ) : ')

        if op not in op_list:
            print('Saisie incorrecte, veuillez recommencer.')

    return op


def ask_number_value(message):
    """
    Demande un nombre à l'utilisateur

    :param message: Message a afficher
    :type message: str

    :return: Nombre
    :rtype: float
    """
    number = None
    while number is None:
        value = input(message + ' : ')

        try:
            number = float(value)
        except Exception:
            number = None
            print('Saisie incorrecte, veuillez recommencer.')

    return number


def ask_yes_no(message):
    """
    Demande à l'utilisateur un oui ou un non

    :param message: Message a afficher
    :type message: str

    :return: True si l'utilisateur entre yes, False si l'utilisateur entre no
    :rtype: bool
    """
    reponse = ''
    while reponse not in ['yes', 'no']:
        reponse = input(message + '( yes | no ) : ')

    return reponse == 'yes'


def do_operation(operator, number1, number2):
    """
    Réalise une operation

    :param operator: Operateur de l'operation ( + | - | / | * )
    :type operator: str

    :param number1: Nombre 1
    :type number1: float

    :param number2: Nombre 2
    :type number2: float

    :return: Résultat de l'opération, ou None en cas d'erreurs
    :rtype: float|None
    """
    if operator == "*":
        return number1 * number2

    if operator == '+':
        return number1 + number2

    if operator == '-':
        return number1 - number2

    if operator == '/':
        if number2 == 0:
            print('<!> Division par zéro impossible')
            return None

        return number1 / number2

    return None


if __name__ == '__main__':
    continuer = True

    print('== Calcultette ==')
    while continuer:
        operateur = ask_operator()
        nb1 = ask_number_value('Entrez le nombre 1')
        nb2 = ask_number_value('Entrez le nombre 2')

        resultat = do_operation(operateur, nb1, nb2)
        print('{0} {1} {2} = {3}\n'.format(nb1, operateur, nb2, resultat))

        continuer = ask_yes_no('Voulez vous continuer ? ')
