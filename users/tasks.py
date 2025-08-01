from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from users.models import User


@shared_task
def check_last_login():
    users = User.objects.filter(last_login__isnull=False)
    present = timezone.now()
    for user in users:
        if present - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
        else:
            print(f"Пользователь {user.email} активен")