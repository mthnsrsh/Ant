import schedule
import time
import datetime


def job():
    TNOW = datetime.datetime.now().replace(microsecond = 0)
    print(str(TNOW) +  "I'm working...")

def job():
    TNOW = datetime.datetime.now().replace(microsecond = 0)
    print(str(TNOW) +  "I love working...")


schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)#

while True:
    schedule.run_pending()
    time.sleep(1)



#to create a reminder / task scheduler
#step 1 - create task with select time
#step 2 - reminder
#step 3 - promts for tasks