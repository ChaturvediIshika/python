import requests
from datetime import datetime
import smtplib

my_email="ishikachaturvedi322@gmail.com"
password="q5oyl3w#RcNw"

def overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    data=response.json()
    lati=float(data["iss_position"]["latitude"])
    longi=float(data["iss_position"]["longitude"])

    if 22<=lati<=32 and 72<=longi<=82:
        return True

def night():
    parameters={
        "lat":27.476219,
        "lng":77.693398,
        "formatted":0
    }

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now=datetime.now().hour
    if time_now>=sunset and time_now<=sunrise:
        return True

if overhead() and night():
    connection=smtplib.SMTP_SSL("smtp.gmail.com",465)
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:LOOK UP!!\n\nThe ISS is above you in the sky..")
    connection.quit()