from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 200.0
PROMISED_UP = 50.0
chrome_driver = "/Users/hariprasath/extension/chromedriver"
complaint_txt="Hii"

bot = InternetSpeedTwitterBot(chrome_driver)
bot.get_internet_speed()
down_speed = float(bot.down)
up_speed = float(bot.up)
print(f'Download Speed = {down_speed} \nUpload Speed   = {up_speed}')

if PROMISED_DOWN > down_speed or PROMISED_UP > up_speed:
    print("complaint initiated")
    bot.tweet_at_provider(complaint_txt)
    print("tweet successful")
