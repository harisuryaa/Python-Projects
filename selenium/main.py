from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver="/Users/hariprasath/extension/chromedriver"

# s=Service(executable_path="/Users/hariprasath/extension/chromedriver")
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.amazon.in/All-new-Echo-Dot/dp/B084L41R96/ref=sr_1_omk_2?adgrpid=118756482901&ext_vrnc=hi&gclid=Cj0KCQjwyMiTBhDKARIsAAJ-9VsEoxiNZzx6F7Jm1UuSbnmu3utyQ4HHKPxJKEqLd7-lOkqMMot2V3caAg9PEALw_wcB&hvadid=590331342657&hvdev=c&hvlocphy=9062142&hvnetw=g&hvqmt=b&hvrand=8988287875354524857&hvtargid=kwd-38411642&hydadcr=4080_2164366&keywords=amazon&qid=1651688704&sr=8-2")

# price = driver.find_element_by_css_selector("span[class='a-price a-text-price a-size-medium apexPriceToPay']")
# price=[p.text for p in price]
# print(price.text)

direct_link=driver.find_element_by_xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]')
print(direct_link.text)
driver.quit()