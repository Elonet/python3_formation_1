# -*- coding: utf-8 -*-

"""exercice3.py

Consignes :

  Créer un CLI permettant d'afficher les données de monitoring de RAM de l'exercice précédant, celui ci devra permettre :

    - Le filtrage par `device_id`
    - Le filtrage par `percent` au dessus ou en dessous d'une valeur fournie en argument

  Les fonctions d'accès aux données et les fonctions d'affichage devront être dans des modules séparés.

Usage :

  pip install -r requirements.txt

Code :
"""

cliDoc = """
Monitoring CLI.

Usage:
  exercice3.py show ram [--device=<device_id> (-p (over|below) <limit>)]
  exercice3.py -h | --help
  exercice3.py --version

Options:
  -p                    Filter per percent.
  -h --help             Show this screen.
  --version             Show version.
  --device=<device_id>  ID of device.
"""

import os
from docopt import docopt
from configobj import ConfigObj
from exercice3_model import get_memory_list
from exercice3_view import show_memory_status_list

basedir = os.path.abspath(os.path.dirname(__file__))
configPath = os.path.join(basedir, 'exercice2.cfg')

if __name__ == '__main__':
    config = ConfigObj(configPath)
    arguments = docopt(cliDoc, version='0.1')

    if arguments['show']:
        if arguments['ram']:

            percent_filter = None
            if arguments['-p']:
                percent_filter = 'over' if arguments['over'] else 'below'

            limit_filter = None
            if arguments['<limit>'] is not None:
                limit_filter = float(arguments['<limit>'])

            try:
                memory_list = get_memory_list(config['server'], arguments['--device'], percent_filter, limit_filter)
                show_memory_status_list(memory_list)

            except Exception as ex:
                print('Erreur durant la récupération des status --> {0}'.format(ex))