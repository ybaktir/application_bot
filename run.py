from app_bot import AppBot
import time
bot = AppBot()
bot.login()
time.sleep(4)
bot.find_jobs()
bot.apply_jobs()