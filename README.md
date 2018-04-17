# Coinmarketcap Price Data Export

The script that builds upon a modified coinmarket scraper (https://github.com/jhogan4288/coinmarketcap-history). It allows to export CSV's of price data on multiple cryptocurrencies listed on coinmarketcap.

# Installation

Running this script as-is requires Python 2 to be available at /usr/bin/python. This is the case by default with macOS.

This script also requires export_coinmarketcap.py, coinmarketcap_usd_history.py and 'cryptos.csv' or any other CSV containing a list of cryptocurrencies installed in same directory

# Usage

Just run in the terminal:
```shell
./export_coinmarketcap.py
```
export_coinmarketcap.py requires code modification to change input parameters.

* `csv_of_cryptocurrencies` is a CSV list of (case-insensitive) names of the currencies / tokens as displayed on CoinMarketCap, with dashes in place of spaces
* `startdate` is the beginning of the range to fetch data for. For example, 2017-10-01 (for 2017 October 10th)
* `enddate` is the end of the range to fetch data for. 

Default data:
csv_of_cryptocurrencies = 'cryptos.csv', uploaded in this repository. It includes a list of all cryptocurrencies listed on coinmarketcap as of 2018-04-16.
startdate = 2014-12-30
enddate = 2018-04-17
