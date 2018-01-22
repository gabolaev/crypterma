from termcolor import colored

from src.config import *
from time import localtime, strftime


def printReport(timeInfo, currencyInfo):
    # this is a result of dirty sex between Python and HTML
    print('\n'+colored('[Bitcoin current rate]', color='white', on_color='on_green', attrs=['bold']))
    print(colored(f'\nUpdate time: {timeInfo["updated"]}','blue'))
    currencyDesc = f'{currencyInfo["description"]}s ({currencyInfo["code"]}'
    print(f'{colored(1,"cyan")} Bitcoin (BTC) == {colored(currencyInfo["rate"], "cyan")} {currencyDesc})')
    print(f'{GRID_LINE*42}')
    print(colored(f'''Please note that the time format is UTC.
It may be different from your region time. \n
Your time is: {strftime("UTC%z (%Z) %H:%M:%S", localtime())}''', 'red'))
    print(f'{GRID_LINE*42}')
    print(colored("Powered by CoinDesk API (https://www.coindesk.com/price)", 'green'))