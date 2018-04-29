import requests
from .configs.config import *
from . import graph, report

def check_ok(response):
    if response.ok:
        return response.json()
    else:
        print(response.text)
        return None # AVE PEP8


def run(start, end, currency='USD'):
    plot_response = check_ok(requests.get(
        url=API_HISTORICAL_URL,
        params=
        {
            'start': start,
            'end': end,
            'currency': currency
        }
    ))

    if not plot_response:
        raise Exception("API error")

    print(f'\nFrom {start} to {end}\n')

    graph.plotting(plot_response['bpi'])

    today_response = check_ok(requests.get(
        url=API_CURRENT_URL.format(f'/{currency}')
    ))

    if not today_response['bpi']:
        raise Exception('API Error')

    yesterday_response = check_ok(requests.get(
        url=API_HISTORICAL_URL,
        params=
        {
            'for': 'yesterday',
            'currency': currency
        }
    ))

    if not yesterday_response['bpi']:
        raise Exception('API Error')

    report.print_report(
        today_response['time'],
        today_response['bpi'][currency],
        list(yesterday_response['bpi'].values())[0])
