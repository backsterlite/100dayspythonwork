from datetime import datetime
from pytz import timezone
import requests, smtplib, ssl, config
from geopy.geocoders import Nominatim
import time

def is_overhead():
    pass

def is_night():
    pass

# Get now time and local timezone

while True:

    now = datetime.now()
    local_timezone = timezone("Europe/Kiev")
    # Get ISS information
    iss_obj = requests.get("http://api.open-notify.org/iss-now.json")
    if iss_obj.status_code != 200:
        iss_obj.raise_for_status()
    else:
        iss_data = iss_obj.json()
        iss_position = {
            'lat': float(iss_data['iss_position']["latitude"]),
            'lng': float(iss_data['iss_position']["longitude"]),
        }
        iss_date = datetime.fromtimestamp(iss_data['timestamp']).astimezone(local_timezone)

    # Get sunrise/sunset information

    parameters = {
        'lat': config.MY_LAT,
        'lng': config.MY_LNG,
        'formatted': 0,
    }
    s_day_obj = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    if s_day_obj.status_code != 200:
        s_day_obj.raise_for_status()
    else:
        s_day_data = s_day_obj.json()
        sunrise = datetime.fromisoformat(s_day_data['results']['sunrise']).astimezone(local_timezone)
        sunset = datetime.fromisoformat(s_day_data['results']['sunset']).astimezone(local_timezone)


    if (config.MY_LAT - 5 <= iss_position['lat'] <= config.MY_LAT + 5) \
        and (config.MY_LNG - 5 <= iss_position['lng'] <= config.MY_LNG + 5):
        print("ISS fly above you")
        if now.hour > sunset and iss_date.hour > sunset :
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as mail:
                mail.login(config.USER, config.PASSWORD)

            print("Look to sky and you will saw ISS")
        else:
            print("ISS fly above you but you can't see it")
    else:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(f"{str(iss_position['lat'])},{str(iss_position['lng'])}")
        print("ISS not fly above you")
        iss_position_c = f"{iss_position['lat']},{iss_position['lng']}"
        print(iss_position_c)
        print(location)
    time.sleep(20)

