import argparse
import sys
import crypterma
from time import localtime, strftime, time
from crypterma.configs import *


def date_with_seconds_shift(seconds=0):
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


def parse_priorities(args):
    namespace = argConfig().parse_args(args)
    currDate = date_with_seconds_shift()

    if namespace.days or namespace.months:
        return date_with_seconds_shift(
            int(namespace.days or 0) * SECONDS_IN_DAY +
            int(namespace.months or 0) * SECONDS_IN_MONTH), \
               currDate, \
               namespace.currency
    else:
        end = namespace.to_date or currDate
        if namespace.from_date or namespace.to_date:
            start = namespace.from_date or BEGINNING
        else:
            start = date_with_seconds_shift(STANDARD_DATE_SHIFT_SECONDS)
        return start, end, namespace.currency


def main(args=None):
    """The main routine."""
    try:
        from_date, to_date, currency = parse_priorities(sys.argv[1:])
        crypterma.core.run(from_date, to_date, currency)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
