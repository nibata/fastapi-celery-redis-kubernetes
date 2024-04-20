from celery import Celery
from time import sleep


celery_app = Celery("workers",
                    broker="redis://redis-service:6379/0",
                    backend="redis://redis-service:6379/0")


@celery_app.task(name="my_tasks", bind=True)
def task_to_perform(self) -> str:
    self.update_state(state="PROGRESS")
    sleep(30)

    return "Task Complete. I counted to 30"
