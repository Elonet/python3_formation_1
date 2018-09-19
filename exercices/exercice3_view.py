# -*- coding: utf-8 -*-

from terminaltables import AsciiTable


def show_memory_status_list(memory_list):
    """
    Affiche la liste des statuts

    :param memory_list:
    """
    head = ['ID', 'Timestamp', 'Device', 'Percent', 'Available', 'Used', 'Free']
    data = [
        [m['id'], m['timestamp'], m['device_id'], m['percent'], m['available'], m['used'], m['free']]
        for m in memory_list
    ]
    table_data = [head]
    table_data.extend(data)

    table = AsciiTable(table_data)
    print(table.table)
