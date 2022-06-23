import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver = "/Users/hariprasath/extension/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument('--profile-dir=~/Library/Application Support/Google/Chrome/Default')
options.add_argument('--user-cache-dir=~/Library/Caches/Google/Chrome/Default')
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)

driver.get("https://web.whatsapp.com/")

time.sleep(15)

#user list
user_list = ["Dinesh Ibs"]
#
# for i in range(1,59):
#     user_list.append(f"T{i}")
#
# print(user_list)

# with open("Input/Letters/starting_letter.txt") as data:
#     msg = data.read()

msg="""Vanakamda \n
mapla hyd la  \n
irunthu"""

file_path="/Users/hariprasath/Downloads/trice_wt.jpeg"

for user_name in user_list:
    try:
        search_by_name=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_by_name.clear()
        search_by_name.send_keys(user_name)
        time.sleep(2)
        search = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        search.click()
        attachment= driver.find_element_by_xpath('//div[@title="Attach"]').click()
        image_bt=driver.find_element_by_xpath('//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_bt.send_keys(file_path)
        time.sleep(2)
        img_text=driver.find_element_by_xpath('//div[@role="textbox"]').send_keys(msg)
        img_send=driver.find_element_by_xpath('//span[@data-icon="send"]').click()
        time.sleep(5)

        ## send_separate txt
        # input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        # input.send_keys(msg)
        # send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        # time.sleep(3)
    except NoSuchElementException:
        pass