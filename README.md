## Celery worker
`celery -A my_tasks:celery_app worker --loglevel=INFO`

## Flowers
`celery -A my_tasks:celery_app flower --port=8001`

## API
`uvicorn main:app --reload`