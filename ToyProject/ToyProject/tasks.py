from celery import Celery, shared_task

@shared_task
def add(x, y):
    return x + y





