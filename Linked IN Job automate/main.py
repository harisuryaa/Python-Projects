import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


chrome_driver="/Users/hariprasath/extension/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument('--profile-dir=~/Library/Application Support/Google/Chrome/Default')
options.add_argument('--user-cache-dir=~/Library/Caches/Google/Chrome/Default')
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)


driver.get("https://www.linkedin.com/jobs/view/3035342819/?eBP=JOB_SEARCH_ORGANIC&refId=IGWYsz4lCZAv58E1xkEuAg%3D%3D&trackingId=Vc4o65uDecNUOgVGTp7S8g%3D%3D")

time.sleep(5)


try:
    apply = driver.find_element_by_css_selector(".jobs-s-apply button").click()
    driver.find_element_by_css_selector("footer button").click()

    time.sleep(3)
    driver.find_elements_by_css_selector("footer button")[1].click()

    driver.find_element_by_css_selector(".fb-single-line-text input").send_keys("1")
    driver.find_elements_by_css_selector("footer button")[1].click()
    driver.find_elements_by_css_selector("footer butto")[1].click()
except NoSuchElementException:
    print("No elements found")