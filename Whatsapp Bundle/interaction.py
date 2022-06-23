from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver="/Users/hariprasath/extension/chromedriver"

# s=Service(executable_path="/Users/hariprasath/extension/chromedriver")
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


# number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# number = driver.find_element_by_css_selector("#articlecount a")
# number.click()

link = driver.find_element_by_link_text("View history")
# link.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()