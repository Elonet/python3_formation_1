# -*- coding: utf-8 -*-

import requests


def get_memory_list(server, device_id=None, filter_percent=None, limit=None):
    """
    Recupere la liste des statuts depuis le serveur

    :param server: Server url
    :type server: str

    :param device_id: Device name
    :type device_id: str|None

    :param filter_percent: Filter per percent
    :type filter_percent: str|None

    :param limit: Limit of filter
    :type limit: float|None

    :return: List of memory status
    :rtype: list
    """
    url = server + '/memory/'
    parameters = '?'

    if device_id is not None:
        parameters += 'device_id=' + device_id

    if filter_percent is not None and limit is not None:
        p = 'percent={0}&target={1}'.format(filter_percent, limit)
        if parameters == '?':
            parameters += p
        else:
            parameters += '&' + p

    if parameters != '?':
        url += parameters

    return requests.get(url).json()['history']
