from celery import Celery,shared_task
import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gtdl.settings')

# app = Celery('gtdl')
app = Celery('ToyProject',
             broker='amqp://',
             backend='amqp://',
             include=['ToyProject.tasks'])

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

def test_print():
    print("TEST")
    return None

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, test_print, name='periodic_test')
