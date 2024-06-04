# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from django.utils.html import format_html

from mail_glint.apps.users.models import User
from mail_glint.bases.admin import Admin


@admin.register(User)
class UserAdmin(Admin, UserAdmin):
    list_display = ('email', 'username')
    search_fields = ('username',)

    fieldsets = (
        ("정보", {"fields": ('email', 'username', 'password', 'thumbnail', 'description')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('email', 'username', 'password', 'thumbnail', 'description')}),
    )
