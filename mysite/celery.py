import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fileSharing.settings')

app = Celery('fileSharing')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-database-every-day': {
        'task': 'mysite.tasks.delete_database',
        'schedule': crontab(day=1),
    },
}