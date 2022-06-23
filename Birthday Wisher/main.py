import smtplib

my_email = ''
passwords = ""

import datetime as dt
import random

now_time=dt.datetime.now()
n=now_time.day

t_time= dt.datetime(year=2022, month=4,day=13)
t=t_time.day

if n == t:
    print("eee")
    with open("quotes.txt","r") as file:
        data = file.readlines()
    print(len(data))
    msgs = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passwords)
        connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com", msg=msgs)



