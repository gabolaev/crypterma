# Now it's just testing file
# Soon there will be an argparse
# You also can change config width and height
# for detailed view on some time intervals


import requests

# TODO: Argument parsing
# TODO: Today plot

import graph
import report
from config import *


def run(start, end, wallet=None):
    plotResponse = requests.get(url=API_PLOT_URL, params={'start': start, 'end': end, 'currency': 'RUB'}).json()
    reportResponse = requests.get(url=API_NOW_URL.format('' if wallet is None else f'/{wallet}')).json()
    graph.plotting(plotResponse['bpi'])
    report.printReport(reportResponse['bpi'])


run('2017-11-06', '2018-01-15', 'RUB')
