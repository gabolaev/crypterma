# Now it's just testing file
# Soon there will be an argparse
# You also can change config width and height
# for detailed view on some time intervals


import requests

# TODO: Pretty ascii plot [DONE]
# TODO: move all the shit to the configuration file [DONE]
# TODO: Dots plot [DONE]
# TODO: Argument parsing
# TODO: Today plot
import graph
from config import *


def run(start, end):
    response = requests.get(url=API_URL, params={'start': start, 'end': end}).json()
    graph.plotting(response['bpi'])


run('2016-08-06', '2017-07-05')
