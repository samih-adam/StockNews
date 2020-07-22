from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


from stocks import send_news

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_news, 'interval', minutes = 30)

sched.start()
