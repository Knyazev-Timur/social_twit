from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'birthday', 'phonenumber', 'created_at', 'update_at')


admin.site.register(User, UserAdmin)