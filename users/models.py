from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    """
           Модель пользователя
           username: CharField - Логин пользователя, обязательное поле
           password: CharField - Пароль, обязательное поле. Обязательно должно содержать не менее 8 символов,
                                 буквы и цифры, так же допустимы спецсимволы.
           phonenumber: PhoneNumberField - Телефонный номер, может отабражаться в национальном или международном формате
           birthday: DateField - Дата рождения, формат: 'YYYY-MM-DD'
           email: EmailField - Почта, валидируется на допустимые домены: ALLOWED_MAIL_DOMAIN
           created_at: DataField - Дата создания поста, заполняется автоматически при создании
           updated_at: DataField - Дата редакции (обновления) поста, заполняется автоматически только при редактировании,
                                   при создании принимает значения null

    """

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
