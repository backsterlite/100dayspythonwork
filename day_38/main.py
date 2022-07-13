import requests
from datetime import datetime

NUTRITIONIX_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_ID = "c0d4dbe4"
NUTRITIONIX_API_KEY = "cdaa5794f368c7a7322c68762546a825"

nutritionix_headers ={
    "x-app-id" : NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json",
}
query = input("Enter your exercises for today: ")
nutritionix_params = {
    "query": query,
    "gender": "male",
    "weight_kg": 93.5,
    "height_cm": 180,
    "age": 29,
}

nutritionix_response = requests.post(NUTRITIONIX_END_POINT, json=nutritionix_params, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
nutritionix_data = nutritionix_response.json()
print(nutritionix_data)
SHEETY_END_POINT = "https://api.sheety.co/e3c902373fd60c5eb2b2e1c285838579/myWorkout/workouts"
today = datetime.now()
now_date = today.strftime("%Y/%m/%d")
now_time = today.strftime("%H:%M:%S")
for exercise in nutritionix_data['exercises']:
    sheety_params = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise['nf_calories']
        }
    }
    sheety_response = requests.post(SHEETY_END_POINT, json=sheety_params)
    sheety_response.raise_for_status()
    print(sheety_response.text)