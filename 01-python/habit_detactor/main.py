import requests
from datetime import datetime
import os
ENDPOINT  = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
H_TEXT =  input("Tell me which exercises you did :")
SHETTY_ENDPOINT_post = os.environ["SHEET_ENDPOINT"]
# BASIC = HTTPBasicAuth("manvendra","@1234Qwer" )
APPROVAL = {    "Authorization": f"Bearer {os.environ['TOKEN']} "
}

# GENDER = "male"
# WEIGHT_KG = "65"
# HEIGHT_CM = "6"
# AGE = "8"

headers = {
    "Content-Type" : "application/json" ,
    "x-app-id"  : APP_ID  ,
    "x-app-key" : API_KEY ,
}

habit_params = {
    "query" : H_TEXT,
    # "gender": GENDER,
    # "weight_kg": WEIGHT_KG,
    # "height_cm": HEIGHT_CM,
    # "age": AGE
}

response =  requests.post(ENDPOINT,json = habit_params,headers=headers)
# print(response.status_code)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHETTY_ENDPOINT_post, json=sheet_inputs,headers=APPROVAL)
    print(sheet_response.text)