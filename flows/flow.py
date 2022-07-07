import prefect
from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule
from prefect.storage import GitHub

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow("my-first-flow") as flow:
    hello_task()

flow.storage = GitHub(
    repo="https://github.com/marcoelumba/prefect.git",
    path="flows/flow.py",                    # location of flow file in repo
    access_token_secret="GITHUB_ACCESS_TOKEN"   # name of personal access token secret
)

#flow.register(project_name="product_graph")
