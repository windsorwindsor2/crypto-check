#simple script that checks crypto preces using the CoinGecko API.

import requests

#Add any crypto that you want a price for to this list.
crypto = ['ethereum', 'bitcoin', 'litecoin', 'dogecoin', 'shiba-inu', 'polkadot']

currency = 'usd'

def crypto_price(name):
    url="https://api.coingecko.com/api/v3/simple/price?ids=" + name + "&vs_currencies=usd"
    response = requests.get(url)
    price = response.json()[name][currency]
    print(f"The current price of {name} is {price} {currency}")

for i in crypto:
    crypto_price(i)