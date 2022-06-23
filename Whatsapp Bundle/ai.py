import os
import openai
def gpt3(stext):
  openai.api_key = ""
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=stext,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
  content=response.choices[0].text.split('.')
  return response.choices[0].text


query = "how are you"
response = gpt3(query)
print(f'response {response}')



# for user_name in user_list:
#     search_by_name=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
#     search_by_name.send_keys(user_name)
#     time.sleep(2)
#     search = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
#     search.click()
#     input= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
#     input.send_keys(msg)
#     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
#     time.sleep(3)
#     search_by_name.clear()