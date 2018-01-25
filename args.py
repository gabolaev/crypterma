import argparse
from time import strftime, localtime, time

from src.config import *


def dateWithSecondsShift(seconds=0):
    return strftime("%Y-%m-%d", localtime(time() - seconds))


def argConfig():
    parser = argparse.ArgumentParser(description='ASCII-chart version of how crypto-currency grows',
                                     epilog="Note, that days/month priority is higher than from/to date's")

    parser.add_argument('-m', '--months', type=int, help='For last N months')
    parser.add_argument('-d', '--days', type=int, help='For last N days')

    parser.add_argument('-f', '--from-date', type=str, help='From date')
    parser.add_argument('-t', '--to-date', type=str, help='To date')

    parser.add_argument('-c', '--currency', default='USD', required=False, type=str, help='Currency code')

    return parser


def parsePriorities(args):
    namespace = argConfig().parse_args(args)

    # in fact, i can write this statement in one line, but it will be a fucking comprehensible piece of shit
    if namespace.days or namespace.months:
        return dateWithSecondsShift(
            int(namespace.days or 0) * SECONDS_IN_DAY +
            int(namespace.months or 0) * SECONDS_IN_MONTH), \
               dateWithSecondsShift(), \
               namespace.currency
    else:
        return namespace.from_date, namespace.to_date, namespace.currency
