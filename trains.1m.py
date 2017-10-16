#!/Users/brenton/.virtualenvs/django-project/bin/python
# -*- coding: utf-8 -*-
import arrow
import requests


tz = 'Australia/Melbourne'  # make this configurable
ROYAL_PARK = ('https://www.ptv.vic.gov.au/langsing/stop-services?stopId=10001169&limit=3&mode=0', 'city')


url, direction = ROYAL_PARK
response = requests.get(url).json()
trains = [
    x for x in response['values']
    if direction.lower() in x['platform']['direction']['direction_name'].lower()
]

train_times = [
    int((arrow.get(x['time_timetable_utc']).to(tz) - arrow.now(tz)).seconds / 60)
    for x in trains
    if arrow.get(x['time_timetable_utc']).to(tz) > arrow.now(tz)
]

for train, time in zip(trains, train_times):
    # trains[0]['platform']['direction']['direction_name']
    print('{}: {}m'.format(train['platform']['stop']['location_name'], str(time)))
    if train == trains[0]:
        print('---')
