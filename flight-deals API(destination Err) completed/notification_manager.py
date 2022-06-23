import requests
from twilio.rest import Client
import smtplib
my_email = ''
passwords = ""

SHEETY_ENDPOINT = "https://api.sheety.co/"



account_sid =""
auth_token = ""


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self,message):
        message = self.client.messages.create(
            body=message,
            from_='whatsapp:',
            to='whatsapp:+919944421125')

        print(message.status)

    def send_emails(self,email, message,link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwords)
            for mail in email:
                connection.sendmail(from_addr=my_email, to_addrs=mail,
                                msg=f"Subject: New Low Price Flight! \n\n{message}\n {link}".encode('utf-8'))
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=passwords)
#     connection.sendmail(from_addr=my_email, to_addrs=email,
#                         msg=f"Subject: New Low Price Flight! \n\n{message}".encode('utf-8'))
