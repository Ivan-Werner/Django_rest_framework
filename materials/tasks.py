from celery import shared_task
from django.core.mail import send_mail
from materials.models import Subscribing
from config.settings import EMAIL_HOST_USER



@shared_task
def update_course_info(course_id):
    subscribing_course = Subscribing.objects.filter(course=course_id)
    print(f"{len(subscribing_course)} подписок на курс {course_id}")
    for subscribing in subscribing_course:
        send_mail(
            subject="Обновление курса",
            message=f"Курс {subscribing.course.title} обновлен",
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscribing.user.email],
            fail_silently=False
        )
