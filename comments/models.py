from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models import User


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.CharField(max_length=1000, verbose_name="Текст")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateField(null=True, verbose_name='Дата изменения')
