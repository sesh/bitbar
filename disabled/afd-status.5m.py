#!/Users/brenton/.virtualenvs/django-project/bin/python

import requests


try:
    response = requests.get('https://shop.aussiefarmers.com.au/welcome/c/131', timeout=10.0)
except requests.exceptions.Timeout:
    response = None
    print('TIMEOUT! | color=#CF0101')
else:
    ref = response.content.rsplit(b'<!-- ')[-2].split(b' -->')[0].decode()
    print('{} {}'.format(response.status_code, ref))
finally:
    if response:
        print('---')
        headers = ['Date', 'Content-Length', 'Server']
        for h in headers:
            if h in response.headers:
                print('{}: {}'.format(h, response.headers.get(h)))

        print('---')
        print('All releases|href=https://delta.brntn.me/track/8cd993ab-0d38-49b7-be67-81dce37b2022')
