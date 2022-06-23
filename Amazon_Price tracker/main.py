from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = ''
passwords = ""

URL="https://www.amazon.com/dp/B08CYD9TR7?tag=camelsearches-20&linkCode=ogi&th=1&psc=1&language=en_US"


header = {
"Accept-Language":"kii",
"User-Agent":"HAri"
}
response = requests.get(url=URL,headers=header)

p=response.content


soup=BeautifulSoup(p,"lxml")
print(soup.prettify())
tag = soup.find_all(class_="a-offscreen")
prices=[usd.getText() for usd in tag]
price_str=prices[1]
price_str=float(price_str.split("$")[1])

print(price_str)
msgs=f"Subject:Hey Look up Amazon \n\n Price For Shoes are low as ${price_str}\n Head over soon {URL}"
if price_str<45:
    print("yes")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passwords)
        connection.sendmail(from_addr=my_email, to_addrs="harisurya631@gmail.com", msg=msgs)
#
#
