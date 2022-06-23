import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime



chrome_driver = "/Users/hariprasath/extension/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument('--profile-dir=~/Library/Application Support/Google/Chrome/Default')
options.add_argument('--user-cache-dir=~/Library/Caches/Google/Chrome/Default')
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)

driver.get("https://web.whatsapp.com/")

time.sleep(10)

#user list
user_list = ["Dinesh Ibs"]
while True:
    for user_name in user_list:
        try:
            search_by_name=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
            search_by_name.clear()
            search_by_name.send_keys(user_name)
            time.sleep(2)
            search = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            search.click()
            time.sleep(3)
            is_online = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
            user_online = is_online.text
            if user_online == "online":
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)

        except NoSuchElementException:
            pass