from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



from comments.models import Comment
from users.models import User


class Post(models.Model):

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.CharField(max_length=1000, verbose_name="Текст")
    images = models.ImageField(upload_to='images/', null=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    comments = models.ManyToManyField(Comment, null=True, verbose_name='Комментарии')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateField(null=True, verbose_name='Дата изменения')
