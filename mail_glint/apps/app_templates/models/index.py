# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from mail_glint.bases.models import Model


class Template(Model):

    class Meta:
        verbose_name = verbose_name_plural = _('템플릿')
        db_table = 'mail_glint'
        ordering = ['-created']
