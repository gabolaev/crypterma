# Now it's just testing file
# Soon there will be an argparse
# You also can change config width and height
# for detailed view on some time intervals


import requests

import graph
import report
from src.config import *


# TODO: Argument parsing
# TODO: Today plot

def run(start, end, wallet=None):
    plotResponse = requests.get(url=API_PLOT_URL, params={'start': start, 'end': end, 'currency': 'RUB'}).json()
    graph.plotting(plotResponse['bpi'])

    reportResponse = requests.get(url=API_NOW_URL.format('' if wallet is None else f'/{wallet}')).json()
    report.printReport(reportResponse['time'], reportResponse['bpi'][wallet])


run('2017-11-14', '2018-01-24', 'RUB')
