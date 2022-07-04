import prefect
from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

schedule = IntervalSchedule(interval=timedelta(minutes=5))

with Flow("hello-flow",  schedule=schedule) as flow:
    hello_task()

flow.run()
