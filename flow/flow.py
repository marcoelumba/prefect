import prefect
from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule
from prefect.storage import GitHub

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

schedule = IntervalSchedule(interval=timedelta(minutes=5))

with Flow("my-first-flow",  schedule=schedule) as flow:
    hello_task()

flow.storage = GitHub(
    path="flows/flow.py",                    # location of flow file in repo
    access_token_secret="GITHUB_ACCESS_TOKEN"   # name of personal access token secret
)

flow.register(project_name="product_graph")
