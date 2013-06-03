'''
Get the local forecast.
'''

import json
import urllib.request

def parse(response):
    obj = json.loads(response)
    weather = {}
    weather['comment'] = obj['weather'][0]['description']
    weather['temp'] = obj['main']['temp']
    weather['max'] = obj['main']['temp_max']
    return weather

def get_weather(location):
    # Feel free to change "imperial" to "metric"
    request_url = ('http://api.openweathermap.org/data/2.5/weather?'
                   'q=%s&units=imperial' %location)
    with urllib.request.urlopen(request_url) as t:
        if t.status == 200:
            result = t.readall().decode('utf-8')
            return parse(result)
        else:
            raise Error('Bad request for weather')

