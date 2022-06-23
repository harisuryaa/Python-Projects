import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 17.400406901674646
MY_LONG = -158.36859656839003
my_email = ''
passwords = ""

DIV_LAT=11.009273854941753
DIV_LONG=76.95929022601052

def check_iss_overhead(MY_LAT=MY_LAT, MY_LONG=MY_LONG):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude,iss_longitude)
    if MY_LAT - 5 <= iss_latitude  <= MY_LAT +5  and  MY_LONG - 5 <= iss_longitude <= MY_LONG +5 :
        return True

def if_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now =str(datetime.now())

    time_now=int(time_now.split(' ')[1].split(":")[0])
    if time_now >= sunset or time_now <=sunrise:
        return True

check_iss_overhead()
if_night()

while True:
    time.sleep(30)
    if check_iss_overhead() :
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwords)
            connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com", msg="Subject:Hey Look up \n\n ISS is above yoou")

    if check_iss_overhead(MY_LONG=DIV_LONG,MY_LAT=DIV_LAT ) :
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwords)
            connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com", msg="Subject:Hey Divya, Look up* \n\n ISS is above yoou Call me!!!")

