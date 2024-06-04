from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticlesConfig(AppConfig):
    name = "mail_glint.apps.articles"
    verbose_name = _('기사 관리')
