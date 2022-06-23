

import pandas
import datetime as dt
import smtplib
import random
now_time = dt.datetime.now()

today_tuple = (now_time.month,now_time.day)
# print(today_tuple)
hbd = pandas.read_csv("birthdays.csv")

new_dict ={(data_row["month"],data_row["day"]):data_row for (index, data_row) in hbd.iterrows()}
bday_person = (new_dict[(4,14)]["name"])
# print(bday_person)
my_email = ''
passwords = ""

if today_tuple in new_dict:
    file_path = f"letter_templates/letter_2.txt"
    with open(file_path, "r") as file:
        contents = file.read()
        contents=contents.replace("[NAME]", bday_person)
        print(contents)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwords)
            connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com", msg=contents)







# while is_on:
#     if today == target_birthday:
#         with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=passwords)
#             connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com", msg=f"Subject: HBD\n\n Hey {b}")
# #



