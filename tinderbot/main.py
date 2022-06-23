import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL=""
FB_PASS=""

chrome_driver="/Users/hariprasath/extension/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://tinder.com/")
sleep(2)
driver.find_element_by_xpath('//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span').click()
sleep(2)
cooke =driver.find_element_by_xpath('//*[@id="q1028785088"]/div/div[2]/div/div/div[1]/div[1]/button/span').click()

try:
    login= driver.find_element_by_xpath('//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]').click()
except NoSuchElementException:
    moreopt = driver.find_element_by_xpath('//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/button').click()
    login= driver.find_element_by_xpath('//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]').click()


base_window = driver.window_handles[0]
sleep(2)
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
fb_email = driver.find_element_by_xpath('//*[@id="email"]')
fb_email.click()
fb_email.send_keys(FB_EMAIL)
fb_pass = driver.find_element_by_xpath('//*[@id="pass"]')
fb_pass.click()
fb_pass.send_keys(FB_PASS)

login_fb=driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

driver.switch_to.window(base_window)
sleep(7)
l_allow = driver.find_element_by_xpath('//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]/span').click()
n_allow=driver.find_element_by_xpath('//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]/span').click()
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="q1028785088"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()