"""
Square Calculator.

Usage:
 squareopt.py <number> [--verbose=<verbose_level>]
 squareopt.py -h | --help
 squareopt.py --version
Options:
 -h --help                  Show this screen.
 --version                  Show version.
 --verbose=<verbose_level>  Verbose level [default: 0].
 """

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')

    answer = int(arguments['<number>']) ** 2
    v_level = int(arguments['--verbose'])

    if v_level == 2:
        print("the square of {} equals {}".format(arguments['<number>'], answer))
    elif v_level == 1:
        print("{}^2 == {}".format(arguments['<number>'], answer))
    else:
        print(answer)