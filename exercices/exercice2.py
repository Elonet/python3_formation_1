# -*- coding: utf-8 -*-

"""exercice2.py

Consignes :
  Créer un script de monitoring de la RAM d'un ordinateur qui envoie les données sur un micro service web.

  La configuration du serveur sera stockée dans un fichier de configuration de votre choix.

  Le script enverra les données au serveur toute les 30 secondes

Micro service : https://github.com/averdier/py_sample_chat_service

Usage :
  pip install -r requirements.txt
  python exercice2.py

Code :
"""

import os
import time
import requests
import psutil
from configobj import ConfigObj

basedir = os.path.dirname(__file__)
configPath = os.path.join(basedir, 'exercice2.cfg')

if __name__ == '__main__':
    config = ConfigObj(configPath)

    while True:
        info = psutil.virtual_memory()

        payload = {
            'device_id': 'pythonbook',
            'timestamp': int(time.time()),
            'total': info.total,
            'percent': info.percent,
            'available': info.available,
            'used': info.used,
            'free': info.free
        }

        try:

            reponse = requests.post(config['server'] + '/memory/', json=payload)

            print('Envoi de : {0} : Response {1}'.format(payload, reponse.status_code))

        except Exception as ex:
            print('Erreur durant l\'envoi des données --> {0}'.format(ex))

        time.sleep(int(config['sleep']))
