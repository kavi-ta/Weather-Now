import requests
import json
from pprint import pprint

def time(lat,lon):
    api_request = requests.get(' http://api.timezonedb.com/v2.1/get-time-zone?key=KM0U3KGCH95P&format=json&by=position&lat='+str(lat)+'&lng='+str(72.85))
    api = json.loads(api_request.content)
    pprint(api)
    #date_time = api['formatted']
    #zone = api['zoneName']
    #print(date_time,zone)
    return

time(lat = 37.57,lon =  126.98)
