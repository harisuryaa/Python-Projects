from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
chrome_driver="/Users/hariprasath/extension/chromedriver"

s=Service(executable_path="/Users/hariprasath/extension/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector("#cookie")
timeout = time.time() + 5   # 5 sec from now
while True:
    clicks = driver.find_element_by_css_selector("#money")
    clicks_int=int(clicks.text)
    print(clicks_int)

    curserss = driver.find_element_by_css_selector("#buyCursor b")
    grandma = driver.find_element_by_css_selector("#buyGrandma b")

    curser_int = curserss.text
    curser_price = int(curser_int.split(" ")[2])
    grandma_int = grandma.text
    grandma_price = int(grandma_int.split(" ")[2])

    cookie.click()

    if time.time() > timeout:
        if grandma_price < clicks_int:
            grandma.click()
            print(f"grandma clicked")
        elif curser_price < clicks_int:
            curserss.click()
            print(f"curser clicked{curser_int}")
        timeout = time.time() + 5
