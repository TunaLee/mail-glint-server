# Django
import uuid
from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from mail_glint.bases.models import Model

# Local

LANGUAGE = (
    ('en', 'English'),
    ('ko', 'Korean'),
    ('cn', 'Chinese'),
    ('vn', 'Vietnam'),
    ('ru', 'Russian')
)


def get_expiration_time():
    return datetime.now() + timedelta(minutes=3)


class SubscriberAuthentication(Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email'), unique=True)
    is_active = models.BooleanField(_('active'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_expiration_time)

    class Meta:
        verbose_name = verbose_name_plural = _('구독자 인증')
        db_table = 'subscriber_authentications'
        ordering = ['-created']


class Subscriber(Model):
    email = models.EmailField(_('email'), unique=True)
    language = models.TextField(_('language'), blank=True, null=True, choices=LANGUAGE)
    send_count = models.IntegerField('count', default=0)

    class Meta:
        verbose_name = verbose_name_plural = _('구독자')
        db_table = 'subscribers'
        ordering = ['-created']
