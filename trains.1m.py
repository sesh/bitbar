#!/Users/brenton/.virtualenvs/bitbar/bin/python
# -*- coding: utf-8 -*-
import arrow
import requests
import sys

from datetime import datetime, time


def print_timetable(url, direction, name):
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
        print('{}: {}m'.format(name, str(time)))
        if train == trains[0]:
            print('---')

    
tz = 'Australia/Melbourne'  # make this configurable
ROYAL_PARK = ('https://www.ptv.vic.gov.au/langsing/stop-services?stopId=10001169&limit=3&mode=0', 'city', 'RP')
BUS_902 = ('https://www.ptv.vic.gov.au/langsing/stop-services?stopId=10013550&direction=Chelsea&limit=3&mode=2', 'chelsea', '902')
BUS_900 = ('https://www.ptv.vic.gov.au/langsing/stop-services?stopId=10010022&direction=Caulfield&limit=3&mode=2', 'caulfield', '900')

current_time = datetime.now().time()

if current_time < time(8, 0):
    print_timetable(*ROYAL_PARK)
elif current_time > time(8, 0) and current_time < time(18, 0):
    print_timetable(*BUS_900)
    print('---')
    print_timetable(*BUS_902)
else:
    sys.exit()
