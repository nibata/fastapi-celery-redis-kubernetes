from fastapi import FastAPI
from modules.my_tasks import celery_app, task_to_perform
import celery.states as states


app = FastAPI()


@app.post("/tasks")
async def send_task():
    task = task_to_perform.delay()

    return {"message": "Task sent successfully", "task_id": task.id}


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)

    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": None
    }

    if task_result.status == states.SUCCESS:
        result["task_result"] = task_result.result

    return result


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    celery_app.control.revoke(task_id, terminate=True)

    return {"message": f"Task {task_id} deleted successfully"}
