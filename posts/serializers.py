from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Post
from posts.validators import ValidationBirthday, ValidationWords


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

#
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
#
#
class PostCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Post
        exclude = ('images',)


    def create(self, validated_data):
        post_data = Post.objects.create(**validated_data)

        birthday = post_data.author.birthday
        title = post_data.title
        text = post_data.text

        birthday_validation = ValidationBirthday(birthday)
        title_validation = ValidationWords(title)
        text_validation = ValidationWords(text)
        if birthday_validation.get_validate_birthday():
            if title_validation.get_validate_words():  # and text_validation.get_validate_words() - При необходимости валидации  и текста
                post_data.title = validated_data['title']
                post_data.text = validated_data['text']
            else:
                raise ValidationError(f"Использование запрещенных слов недопустимо!")
        else:
            raise ValidationError(f"Публикация постов разрешена с 18 лет!")

        post_data.save()
        return post_data


class PostUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    update_at = serializers.DateField(read_only=True)

    class Meta:
        model = Post
        exclude = ("images",)

    def update(self, instance: Post, validated_data: dict) -> Post:

        instance.author = validated_data['author']

        comments = tuple(validated_data.get('comments', []))
        instance.comments.set([comment.id for comment in comments])
        title = validated_data['title']
        text = validated_data['text']
        birthday = instance.author.birthday

        birthday_validation = ValidationBirthday(birthday)
        title_validation = ValidationWords(title)
        text_validation = ValidationWords(text)
        if birthday_validation.get_validate_birthday():
            if title_validation.get_validate_words(): #and text_validation.get_validate_words() - При необходимости валидации  и текста
                instance.title = validated_data['title']
                instance.text = validated_data['text']
            else:
                raise ValidationError(f"Использование запрещенных слов недопустимо!")
        else:
            raise ValidationError(f"Публикация постов разрешена с 18 лет!")

        instance.save()
        return instance



class PostDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id']
