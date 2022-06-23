from instafollower import InstaFollower

USERNAME = ""
PASSWORD = ""

SIMILAR_ACC= "chefsteps"

chrome_driver = "/Users/hariprasath/extension/chromedriver"

bot = InstaFollower(chrome_driver)
# bot.login(USERNAME, PASSWORD)

bot.find_follower(SIMILAR_ACC)
bot.follow()

