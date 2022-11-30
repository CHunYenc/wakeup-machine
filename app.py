from apscheduler.schedulers.blocking import BlockingScheduler
from urllib import request
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log.txt",
    filemode="w",
    format="[%(asctime)s] %(levelname)s - %(message)s")


def scheduled_job():
    url = os.environ.get("URL","http://your.domain.com")
    request.urlopen(url)
    logging.info(f"連線成功!")


if __name__ == "__main__":
    # 先執行一次
    scheduled_job()
    # 宣告一個排程
    sched = BlockingScheduler(timezone="Asia/Taipei")
    # 定義排程 : 在周一至周五，每 20 分鐘就做一次 def scheduled_jog()
    sched.add_job(scheduled_job, "cron", day_of_week="mon-fri", minute="*/10")
    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass
