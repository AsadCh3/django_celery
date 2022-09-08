from __future__ import absolute_import, unicode_literals
from asyncio.log import logger


import random
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep


# Here is the command to run scheduler
# celery -A myproj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler



@shared_task
def add(x, y):
    # Celery recognizes this as the `movies.tasks.add` task
    # the name is purposefully omitted here.
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total