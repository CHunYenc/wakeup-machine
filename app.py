from apscheduler.schedulers.blocking import BlockingScheduler
from urllib import request
import os
import logging
import variables

logging.basicConfig(
    level=logging.INFO,
    filename="scheduler.log",
    filemode="w",
    format="[%(asctime)s] %(levelname)s - %(message)s")


def scheduled_job():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    url = variables.URL
    req = request.Request(url=url, headers=headers)
    try:
        request.urlopen(req).read()
    except Exception as e:
        logging.info(f"{e}")
    else:
        logging.info(f"Successful connection {url}.")


if __name__ == "__main__":
    # run once
    scheduled_job()
    # init Scheduler
    sched = BlockingScheduler(timezone="Asia/Taipei")
    # add job
    sched.add_job(scheduled_job, "cron",
                  year=variables.APSCHEDULER_YEAR,
                  month=variables.APSCHEDULER_MONTH,
                  day=variables.APSCHEDULER_DAY,
                  week=variables.APSCHEDULER_WEEK,
                  day_of_week=variables.APSCHEDULER_DAY_OF_WEEK,
                  hour=variables.APSCHEDULER_HOUR,
                  minute=variables.APSCHEDULER_MINUTE,
                  second=variables.APSCHEDULER_SECOND)
    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass
