# knowing conversion value of bitcoin with USD
# in this script we have used request module
# you need to install requests module using pip install requests

import requests
res = requests.get("https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD")

price = res.json()

pr = price["last"]

print('Last Rates of Bitcoin {0:.0f} m'.format(pr))


                   
