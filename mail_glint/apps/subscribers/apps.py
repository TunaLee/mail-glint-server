from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SubscribersConfig(AppConfig):
    name = "mail_glint.apps.subscribers"
    verbose_name = _('구독자 관리')
