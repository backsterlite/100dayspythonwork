import config
import requests
import os

# Get Wether Data

parameters = {
    "lat": config.MY_LAT,
    "lon": config.MY_LNG,
    "appid": config.OWM_API_KEY,
    "lang": "UA",
    "units": "metric",
    "exclude": "daily,minutely,current",

}
owm_obj = requests.get(config.OWM_ENDPOINT, params=parameters)
owm_obj.raise_for_status()
owm_data = owm_obj.json()
ids = list(map(lambda x: x['weather'][0]["id"], owm_data['hourly']))

will_rain = False
for id in ids:
    if id < 700:
        will_rain = True

if will_rain:
    print("Will rain, don't forger a take ☔")


