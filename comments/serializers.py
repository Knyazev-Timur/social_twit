from datetime import date

from rest_framework import serializers

from comments.models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment_data = Comment.objects.create(**validated_data)

        comment_data.save()
        return comment_data


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):

    comment = Comment.objects.all()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
    def save(self):
        comment = super().save()
        comment.update_at = date.today()
        comment.save()
        return comment


class CommentDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id']


