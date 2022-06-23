from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver="/Users/hariprasath/extension/chromedriver"

# s=Service(executable_path="/Users/hariprasath/extension/chromedriver")
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.python.org/")

event_time =driver.find_elements_by_css_selector('.event-widget time')
event_name =driver.find_elements_by_css_selector('.event-widget li a')
events={}
for n in range(len(event_time)):
    events[n]={
        "time":event_time[n].text,
            "Name":event_name[n].text
    }
print(events)


driver.quit()