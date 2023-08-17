from datetime import date

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from users.models import User
from users.validators import ValidationPassword, ValidationEmail


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        email = user.email

        password_validation = ValidationPassword(password)
        if password_validation.get_validate_password():
            user.set_password(user.password)
        else:
            raise ValidationError(f"Пароль не может быть менее 8 символов, должен содержать цифры и буквы!")

        email_validation = ValidationEmail(email)
        if email_validation.get_validate_email():
            user.email = validated_data['email']
        else:
            raise ValidationError(f"Допустимые почтовые домены: 'mail.ru' или 'yandex.ru'!")

        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phonenumber', 'birthday', 'email', 'is_staff']



class UserDetailSerializer(serializers.ModelSerializer):

    user = User.objects.all()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phonenumber', 'birthday', 'email', 'created_at', 'update_at', 'is_staff']


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = User
        # exclude = ('created_at',)
        fields = ['id', 'username', 'password', 'phonenumber', 'birthday', 'email', 'created_at', 'update_at', 'is_staff']

    def update(self, instance: User, validated_data: dict) -> User:

        instance.username = validated_data['username']
        password = validated_data['password']


        instance.phonenumber = validated_data['phonenumber']
        instance.birthday = validated_data['birthday']
        email = validated_data['email']
        instance.update_at = date.today()
        instance.is_staff = validated_data['is_staff']

        password_validation = ValidationPassword(password)
        if password_validation.get_validate_password():
            instance.set_password(instance.password)
        else:
            raise ValidationError(f"Пароль не может быть менее 8 символов, должен содержать цифры и буквы!")


        email_validation = ValidationEmail(email)
        if email_validation.get_validate_email():
            instance.email = validated_data['email']
        else:
            raise ValidationError(f"Допустимые почтовые домены: 'mail.ru' или 'yandex.ru'!")

        instance.save()
        return instance



class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
