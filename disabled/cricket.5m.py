#!/Users/brenton/.virtualenvs/bitbar/bin/python
import requests

response = requests.get("http://site.api.espn.com/apis/site/v2/sports/cricket/10883/summary?contentorigin=espn&event=1072307&lang=en&region=au&section=cricinfo").json()
score = response['header']['title'].split(' (')[0]
print(score)
print('---')
print('Cricinfo|href=http://www.espncricinfo.com/series/10883/game/1072307/australia-vs-england-3rd-test-eng-tour-of-aus-and-nz-2017-18/')
