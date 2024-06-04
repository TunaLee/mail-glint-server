# Django
import os
from time import strftime, gmtime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from mail_glint.apps.users.models.fields.phone_number import CustomPhoneNumberField
from mail_glint.apps.users.models.managers.active import UserActiveManager
from mail_glint.apps.users.models.managers.objects import UserMainManager
from mail_glint.bases.models import Model


def image_path(instance, filename):
    upload_to = 'GlintNews/Author'
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(upload_to, filename)
# Class Section
class User(AbstractUser,
           Model):
    email = models.EmailField(_('이메일'), unique=True, null=True, blank=True)
    username = models.CharField(_('닉네임'), unique=True, max_length=100, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)
    thumbnail = models.ImageField(upload_to=image_path, null=True)
    description = models.TextField(_('작가소개'), null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserMainManager()
    active = UserActiveManager()

    class Meta:
        verbose_name = verbose_name_plural = _('유저')
        db_table = 'users'
        ordering = ['-created']

    def __str__(self):
        return self.username
