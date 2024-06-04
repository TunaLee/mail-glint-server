# Django
import os
from time import gmtime, strftime

from django.db import models
from django.utils.translation import gettext_lazy as _


def image_path(instance, filename):
    upload_to = 'GlintNews/Articles/ThumbNail'
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(upload_to, filename)


class ArticleModelMixin(models.Model):
    class Meta:
        abstract = True

    title = models.TextField(_('제목'))
    subtitle = models.TextField(_('부제목'), blank=True, null=True)
    content = models.TextField(_('내용'), blank=True, null=True)
    thumbnail = models.ImageField(upload_to=image_path)
    views = models.PositiveIntegerField(_('조회수'), default=0)
    likes = models.PositiveIntegerField(_('좋아요 수'), default=0)
