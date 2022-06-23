import time
import requests
import queue
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys

URL = 'https://www.zillow.com/san-francisco-ca/rental-buildings/'
DOCS=""

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument('--profile-dir=~/Library/Application Support/Google/Chrome/Default')
options.add_argument('--user-cache-dir=~/Library/Caches/Google/Chrome/Default')

chrome_driver = "/Users/hariprasath/extension/chromedriver"

header = {
"Accept-Language":"en-IN",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}
response = requests.get(url=URL,headers=header)

web_data = response.content
soup = BeautifulSoup(web_data, "html.parser")

links=[]
text = []
price=[]
data = soup.find_all(class_="list-card-addr")
for d in data:
    text.append(d.getText())
print(text)

data2=soup.find_all(class_="list-card-price")

for d2 in data2:
    price.append(d2.getText())
print(price)
print(len(price))

data3=soup.find_all(name='a',class_="list-card-link")
for d3 in data3:
    links.append(d3.get('href'))
links=links[::2]
full_link=[]
for l in links:
    if "http" not in l:
        full_link.append(f"https://www.zillow.com{l}")
    else:
        full_link.append(l)

print(full_link)

driver = webdriver.Chrome(executable_path=chrome_driver)

for n in range(len(full_link)):
    driver.get(DOCS)

    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(text[n])
    prices.send_keys(price[n])
    link.send_keys(full_link[n])
    submit_button.click()
