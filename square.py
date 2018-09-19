import argparse

# From https://docs.python.org/fr/3/howto/argparse.html

# Définition des arguments

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")

if __name__ == '__main__':
    # Traitement des arguments
    args = parser.parse_args()
    answer = args.square ** 2

    if args.verbosity == 2:
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)
