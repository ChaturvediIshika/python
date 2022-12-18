import smtplib

my_email="ishikachaturvedi322@gmail.com"
password="q5oyl3w#RcNw"

connection=smtplib.SMTP_SSL("smtp.gmail.com",465)
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="anikateag7316@gmail.com", msg="Subject:Hello!\n\n how are you?")
connection.quit()