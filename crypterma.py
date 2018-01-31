#!/usr/local/bin/python3
# Now it's just testing file
# Soon there will be an arg parse
# You also can change config width and height
# for detailed view on some time intervals


import sys

import requests

import args
import graph
import report
from src.config import *


def checkOk(response):
    if response.ok:
        return response.json()
    else:
        print(response.text)


def run(start, end, currency='USD'):

    plotResponse = checkOk(requests.get(
        url=API_HISTORICAL_URL,
        params=
        {
            'start': start,
            'end': end,
            'currency': currency
        }
    ))

    if not plotResponse:
        return

    print(f'\nFrom {start} to {end}\n')

    graph.plotting(plotResponse['bpi'])

    todayResponse = checkOk(requests.get(
        url=API_CURRENT_URL.format(f'/{currency}')
    ))

    if not todayResponse['bpi']:
        return print('API Error')

    yesterdayResponse = checkOk(requests.get(
        url=API_HISTORICAL_URL,
        params=
        {
            'for': 'yesterday',
            'currency': currency
        }
    ))
    if not yesterdayResponse['bpi']:
        return print('API Error')

    report.printReport(todayResponse['time'],
                       todayResponse['bpi'][currency],
                       list(yesterdayResponse['bpi'].values())[0])


try:
    from_date, to_date, currency = args.parsePriorities(sys.argv[1:])
    run(from_date, to_date, currency)

except Exception as ex:
    print(ex)
