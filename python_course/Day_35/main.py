import requests
import smtplib

my_email="ishikachaturvedi322@gmail.com"
password="q5oyl3w#RcNw"

my_api="92374ecbd718808f3994924f72d29590"

parameters={
    "lat":27.476219,
    "lon":77.693398,
    "exclude":"current,monthly,minutely",
    "appid":my_api
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data=response.json()
for i in range(12):
    a=data["hourly"][i]["weather"][0]["id"]
    if a<700:
        connection=smtplib.SMTP_SSL("smtp.gmail.com",465)
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="cishika104@gmail.com", msg="Subject:Rain Alert!!\n\nBring your umbrella today.")
        connection.quit()
        break
