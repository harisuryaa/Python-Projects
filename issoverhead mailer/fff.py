import smtplib


my_email = 'hari.prasath.e01@gmail.com'
passwords = "ozqfbzgcomatlvqu"

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=passwords)
    connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com",
                        msg="Subject:Open \n\n Hello this is a sample mail")


# with smtplib.SMTP("smtp.mail.yahoo.com", 2525) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=passwords)
#     connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com",
#                         msg="Subject:Open pandra sunni \n\n umbu da punda")