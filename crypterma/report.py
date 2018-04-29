from time import localtime, strftime

from termcolor import colored

from .configs.config import *


def print_report(time_info, currency_today, price_yesterday):
    # this is a result of dirty sex between Python and HTML
    print('\n' + colored('[Bitcoin current rate]', color='white', on_color='on_green', attrs=['bold']))
    print(colored(f'Update time: {time_info["updated"]}', 'blue'),
          colored(f'(Your time is: {strftime("UTC%z (%Z) %H:%M:%S", localtime())})\n', 'red'))

    difference = currency_today['rate_float'] - price_yesterday
    currency_desc = f'{currency_today["description"]}s ({currency_today["code"]}'

    print(f'{colored(1,"cyan")} Bitcoin (BTC) == {colored(currency_today["rate"], "cyan")} {currency_desc})')
    print(f'Yesterday it was {"more expensive for" if difference < 0 else "cheaper by"} {round(abs(difference), 3)}')
    print(f'{GRID_LINE*42}')
    print(colored("Powered by CoinDesk API (https://www.coindesk.com/price)\n", 'green'))
