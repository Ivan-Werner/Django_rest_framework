from tabnanny import verbose

from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson


class User(AbstractUser):
    user_name = None
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    TYPE_CHOICES = [
        ('cache', 'наличные'),
        ('transfer', 'перевод')


    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплаченный урок')
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Тип оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

