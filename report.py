from time import localtime, strftime

from termcolor import colored

from src.config import *


def printReport(timeInfo, currencyToday, priceYesterday):
    # this is a result of dirty sex between Python and HTML
    print('\n' + colored('[Bitcoin current rate]', color='white', on_color='on_yellow', attrs=['bold']))
    print(colored(f'Update time: {timeInfo["updated"]}', 'blue'), colored(f'(Your time is: {strftime("UTC%z (%Z) %H:%M:%S", localtime())})\n', 'red'))

    difference = currencyToday['rate_float'] - priceYesterday
    currencyDesc = f'{currencyToday["description"]}s ({currencyToday["code"]}'

    print(f'{colored(1,"cyan")} Bitcoin (BTC) == {colored(currencyToday["rate"], "cyan")} {currencyDesc})')
    print(f'Yesterday it was {"more expensive for" if difference < 0 else "cheaper by"} {abs(difference)}')
    print(f'{GRID_LINE*42}')
    print(colored("Powered by CoinDesk API (https://www.coindesk.com/price)\n", 'green'))
