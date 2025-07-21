from django.db import models
from django.db.models import ForeignKey, SET_NULL

from django.contrib.auth import get_user_model

from config import settings


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название",
        help_text="Введите название",
    )
    preview = models.ImageField(
        upload_to="materials/preview/course",
        blank=True,
        null=True,
        verbose_name="Превью",
    )
    description = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание",
    )
    link_to_video = models.URLField(
        verbose_name="Ссылка на видео", blank=True, null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=SET_NULL,
        verbose_name="Курс",
        blank=True,
        null=True,
        related_name="lessons",
    )
    description = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )
    preview = models.ImageField(
        upload_to="materials/preview/lesson",
        blank=True,
        null=True,
        verbose_name="Превью урока",
    )
    link_to_video = models.URLField(
        verbose_name="Ссылка на видео", blank=True, null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
