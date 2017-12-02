from celery import Celery
from celery.decorators  import periodic_task
from datetime           import timedelta
app = Celery('test', broker='pyamqp://guest@localhost//')

from celery import shared_task
@shared_task
def add(x, y):
    print(x + y)
    add.apply_async((x, y,), countdown=5)