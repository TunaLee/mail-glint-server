from django.contrib import admin

from mail_glint.apps.subscribers.models import Subscriber
from mail_glint.bases.admin import Admin


@admin.register(Subscriber)
class SubscriberView(Admin):
    list_display = ('email',)
    search_fields = ('',)
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('',)}),
    )
