from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe

from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author_link', 'images', 'display_comments', 'created_at', 'update_at')
    list_filter = ('created_at',)

    def author_link(self, obj: Post) -> str:
        url = reverse('admin:users_user_change', args=[obj.author.id])
        link = f'<a href="{url}">{obj.author}</a>'
        return mark_safe(link)

    author_link.short_description = 'Автор'


admin.site.register(Post, PostAdmin)
