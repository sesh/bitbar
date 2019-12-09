#!/Users/brenton/.virtualenvs/bitbar/bin/python
# -*- coding: utf-8 -*-

import pytz
from datetime import datetime

timezones = [
  ('Asia/Kolkata', 'Bangalore'),
  ('Europe/London', 'London'),
  ('Australia/Melbourne', 'Melbourne'),
  ('Europe/Berlin', 'Germany'),
  ('America/New_York', 'New York'),
  ('America/Los_Angeles', 'L.A.')
]

now = datetime.utcnow().replace(tzinfo=pytz.utc)

first = True
for tz, city in timezones:
    print(f"{city}: {now.astimezone(pytz.timezone(tz)).strftime('%H:%M')}")
    if first:
        print('---')
        first = False
