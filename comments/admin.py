from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at', 'update_at')


admin.site.register(Comment, CommentAdmin)