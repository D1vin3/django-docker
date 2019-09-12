from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone


@periodic_task(run_every=crontab(minute='*'))
def hello_world():
    print('hello world')
    return 'hello world'
