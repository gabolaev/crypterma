# <div align="center">crypterma</div>
#### ASCII-chart version of how crypto-currency grows
A console application that allows you to see a graph of the Bitcoin price change in any time interval. Also prints the current cost and comparison with yesterday's value.
Almost all currencies are supported.
###### Required Python3.6 and upper
#### install:
pip install crypterma
###### examples:
```bash
crypterma -f 2013-10-13 -t 2017-01-02 -c RUB # from 13 October 2013 to 2 January 2017 in Russian Rubles
crypterma -f 2012-05-20 -c USD               # from 20 May 2012 until today in United States Dollars
crypterma -t 2015-08-14 -c BYR               # from beginning to 14 August 2015 in Belarusian Ruble
crypterma -m 3 -d 14 -c EUR                  # for the last 3 months and 14 days in Euros
crypterma -d 500 -c AED                      # for the last 500 days in United Arab Emirates Dirhams
crypterma -m 6 -c UZS                        # for the last 6 months in Uzbekistan Soms
crypterma                                    # for the last 2 months in United States Dollars
```

<img src="https://github.com/gabolaev/crypterma/blob/master/src/example.png">
