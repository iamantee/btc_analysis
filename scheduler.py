from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

def job_aave_borrow_alert():
    subprocess.run(['python3', 'tgbot-aave.py'])

scheduler = BlockingScheduler()
scheduler.add_job(job_aave_borrow_alert, 'cron', hour=0, minute=21)
scheduler.start()



