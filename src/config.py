WIDTH = 100
HEIGHT = 40
COUNT_OF_DATES = 4
DATE_LENGTH = 12
COLORS = ['magenta', 'red', 'yellow', 'green', 'blue', 'cyan', None]

CHART_LINE = '█'
GRID_LINE = '-'
CHART_LEFT_BORDER = '║-'
CHART_LOWER_BORDER = '═'

API_HISTORICAL_URL = 'https://api.coindesk.com/v1/bpi/historical/close.json'

API_CURRENT_URL = 'https://api.coindesk.com/v1/bpi/currentprice{}.json'
DISCLAIMER = 'This data was produced from the CoinDesk Bitcoin Price Index (USD).\nNon-USD currency data converted ' \
             'using hourly conversion rate from openexchangerates.org '

STANDARD_DATE_SHIFT_SECONDS = 5184000
SECONDS_IN_MONTH = 2678400
SECONDS_IN_DAY = 86400
