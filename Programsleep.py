import time
import schedule
import botFrom


def job():
    botFrom.bot.login()
    botFrom.bot.fillin()


#schedule.every().minute.at(":17").do(job)
#schedule.every().day.at("10:30").do(job)
schedule.every().day.at("7:32").do(job)
schedule.every().day.at("20:18").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
