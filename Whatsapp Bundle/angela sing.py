from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_driver="/Users/hariprasath/extension/chromedriver"

# s=Service(executable_path="/Users/hariprasath/extension/chromedriver")
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Hari")
second_name = driver.find_element_by_name("lName")
second_name.send_keys("Prasath")
email = driver.find_element_by_name("email")
email.send_keys("hari@gamail.com")
button = driver.find_element_by_xpath('/html/body/form/button')
button.click()

driver.quit()

