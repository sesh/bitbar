#!/Users/brenton/.virtualenvs/bitbar/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# just here for reference: Olympic Park observations
OLYMPIC_PARK = 'http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json'


response = requests.get('http://www.bom.gov.au')
soup = BeautifulSoup(response.content, 'html.parser')

capitals = soup.find_all(attrs={'class': 'capital'})
melbourne = capitals[1]
now = melbourne.find(attrs={'class': 'now'})
temp = now.findChild().text.replace('°', '')

max_temp = melbourne.find_all(attrs={'class': 'max'})[-1].text.replace('°', '')

print(temp + 'C')
print('---')
print(melbourne.find('h3').text + ': ' + melbourne.find(attrs={'class': 'precis'}).text)
print('Currently: {}. Max: {}'.format(temp, max_temp))
print(melbourne.find(attrs={'class': 'wind'}).text)
print('---')
print('Home Temperature|href=http://home-temperature.glitch.me/')
print('BOM Forecast|href=http://www.bom.gov.au/vic/forecasts/melbourne.shtml')
print('BOM Radar|href=http://www.bom.gov.au/products/IDR023.loop.shtml')
print('BayWX Chart|href=http://www.baywx.com.au/melbtemp2.html')
