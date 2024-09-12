import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 19.391928
MY_LONG = 72.839729
FORMAT = 0
MY_EMAIL = "patilaniket209@gmail.com"
MY_PASSWORD = "zepu snzt qpij rtin"


def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    data_iss = response_iss.json()

    longitude = float(data_iss["iss_position"]["longitude"])
    latitude = float(data_iss["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": 19.391928,
        "lng": 72.839729,
        "formatted": FORMAT,
    }


    response = requests.get("https://api.sunrise-sunset.org/json",
                           params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up\n\nThe ISS is above you in the sky!"
        )

