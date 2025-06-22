import os
from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_notifier.settings')

app = Celery('bot_notifier')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()