from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(username, email):
    subject = 'Welcome to Bot Notifier!'
    message = f'Hi {username}, thank you for registering with Bot Notifier!'
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],  # Use the user's email
        fail_silently=False,
    )