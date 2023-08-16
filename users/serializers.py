from datetime import date

from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'birthday', 'phonenumber', 'is_staff']


class UserDetailSerializer(serializers.ModelSerializer):

    user = User.objects.all()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phonenumber', 'birthday', 'created_at', 'update_at']


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = User
        # exclude = ('created_at',)
        fields = ['id', 'username', 'password', 'phonenumber', 'birthday', 'created_at', 'update_at']
    def save(self):
        user = super().save()
        user.update_at = date.today()
        user.set_password(user.password)
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


