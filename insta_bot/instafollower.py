import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument('--profile-dir=~/Library/Application Support/Google/Chrome/Default')
options.add_argument('--user-cache-dir=~/Library/Caches/Google/Chrome/Default')

class InstaFollower:
    def __init__(self,chrome_driver):
        self.driver = webdriver.Chrome(executable_path=chrome_driver, options=options)

    def login(self, USERNAME, PASSWORD):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_follower(self,SIMILAR_ACC):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")
        time.sleep(2)
        prs_follower = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(2)

        modal = self.driver.find_element_by_xpath("//div[@Class='isgrP']")
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons =  self.driver.find_elements_by_css_selector('li button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                prs_cancel = self.driver.find_element_by_xpath('//button[text()="Cancel"]').click()