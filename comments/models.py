from django.db import models

from users.models import User


class Comment(models.Model):
    """
    Модель коментарии
    author: ForeignKey - указание, на пользователя создавшего комментарий
    text: CharField - текстовое поле комментария, максимальная длинна 1000 символов
    created_at: DataField - Дата создания комментария, заполняется автоматически при создании
    updated_at: DataField - Дата редакции (обновления) коментария, заполняется автоматически только при редактировании,
                            при создании принимает значения null
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.CharField(max_length=1000, verbose_name="Текст")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateField(null=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
