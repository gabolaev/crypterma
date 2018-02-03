import requests
from .configs.config import *
from . import graph, report

def checkOk(response):
    if response.ok:
        return response.json()
    else:
        print(response.text)
        return None # AVE PEP8


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
