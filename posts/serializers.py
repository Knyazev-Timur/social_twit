from datetime import date

from rest_framework import serializers

from posts.models import Post


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

        post_data.save()
        return post_data


class PostUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Post
        exclude = ('images',)

    def save(self):
        post = super().save()
        post.update_at = date.today()

        post.save()
        return post


class PostDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id']
