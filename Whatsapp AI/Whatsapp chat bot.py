import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
no= 1
chrome_driver = "/Users/hariprasath/extension/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
options.add_argument('--profile-dir=~/Library/Application Support/Google/Chrome/Default')
options.add_argument('--user-cache-dir=~/Library/Caches/Google/Chrome/Default')
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)

driver.get("https://web.whatsapp.com/")

time.sleep(15)
user_name = "Ibs"
# msg = "Aparna chote bachi ho kya"
used_word=[]

import openai
ai = False

def gpt3(stext):
    openai.api_key = "sk-"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=stext,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    content = response.choices[0].text.split('.')
    return response.choices[0].text

last_msg=""

def whatsapp():
    global ai
    global last_msg
    search_by_name = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_by_name.send_keys(user_name)
    time.sleep(2)
    try:
        last_text = driver.find_element_by_xpath(
            '//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div[2]/div[2]/div[1]/span/span[3]')
        last_msg = last_text.text
    except NoSuchElementException:
        ai = False
        pass

    if last_msg not in used_word:
        used_word.append(last_msg)
        ai= True
    else:
        ai = False
    time.sleep(3)
    search_by_name.clear()
    return used_word[len(used_word)-1], ai

t=True

while t:
    query = whatsapp()[0]
    print(no)
    no=no+1
    print(ai)
    if ai:

        print(query)
        response = gpt3(query)
        search = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        search.click()
        input= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        input.send_keys(response)
        send=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()






