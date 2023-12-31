from django.db import models

from comments.models import Comment
from users.models import User


class Post(models.Model):
    """
       Модель постов
       title: Charfield - заголовок поста, максимальная длинна 100 символов, валидируется при создании и редактировании
                          на запрещенные слова: STOP_LIST_WORDS
       text: CharField - текст поста, максимальная длинна 1000 символов
       author: ForeignKey - указание, на пользователя создавшего комментарий
       comments: ManyToManyField - перечень ID комментариев к посту
       created_at: DataField - Дата создания поста, заполняется автоматически при создании
       updated_at: DataField - Дата редакции (обновления) поста, заполняется автоматически только при редактировании,
                               при создании принимает значения null
    """

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.CharField(max_length=1000, verbose_name="Текст")
    images = models.ImageField(upload_to='images/', null=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    comments = models.ManyToManyField(Comment, default=None, verbose_name='Комментарии')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateField(null=True, verbose_name='Дата изменения')


    def display_comments(self):
        return '; '.join([comment.text for comment in self.comments.all()])
    display_comments.short_description = 'Комментарии'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
