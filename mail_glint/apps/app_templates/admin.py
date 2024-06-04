from django.contrib import admin

from mail_glint.bases.admin import Admin


@admin.register(Template)
class TemplateView(Admin):
    list_display = ('',)
    search_fields = ('',)
    readonly_fields = ('',)

    fieldsets = (
        ("정보", {"fields": ('',)}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('',)}),
    )
