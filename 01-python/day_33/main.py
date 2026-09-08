# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if  response.status_code == 404:
# #     raise Exception("That resorce does not exit .")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this  data .")
# # response.raise_for_status()
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
#
# print(iss_position)

import requests
from datetime import datetime

MY_LAT =26.921039
MY_LONG =75.794359


parameters =  {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}



response = requests.get(url=" https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =  data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
