#!/Users/brenton/.virtualenvs/runsync/bin/python
import requests


books = [
    'ETH-USD', 'BTC-USD', 'LTC-USD',
]


for b in books:
    response = requests.get(f'https://api.gdax.com/products/{b}/ticker').json()
    print('{} {:.2f}'.format(b, float(response['price'])))
