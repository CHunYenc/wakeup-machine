from apscheduler.schedulers.blocking import BlockingScheduler
from urllib import request
import os

def scheduled_job():
    url = "https://{{ 你的 onrender 網址}}.onrender.com/"
    request.urlopen(url)

if __name__ == '__main__':
    # 宣告一個排程
    sched = BlockingScheduler(timezone="Asia/Taipei")
    # 定義排程 : 在周一至周五，每 20 分鐘就做一次 def scheduled_jog()
    sched.add_job(scheduled_job, 'cron', day_of_week='mon-fri', minute="*/10")
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass