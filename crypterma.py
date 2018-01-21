# Now it's just testing file
# Soon there will be an argparse
# You also can change config width and height
# for detailed view on some time intervals


import requests

# TODO: Argument parsing
# TODO: Today plot

import graph
from config import *


def run(start, end):
    response = requests.get(url=API_URL, params={'start': start, 'end': end, 'currency': 'RUB'}).json()
    graph.plotting(response['bpi'])


run('2017-11-06', '2018-01-15')
