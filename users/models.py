from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):

    phonenumber = PhoneNumberField(unique=True, verbose_name='Телефон')
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(unique=True, max_length=64, verbose_name="e-mail")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateField(null=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
