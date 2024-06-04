# Django
import os
from time import gmtime, strftime

from django.db import models
from django.utils.translation import gettext_lazy as _

from mail_glint.apps.articles.models.mixins.article import ArticleModelMixin
# Local
from mail_glint.bases.models import Model


def image_path(instance, filename):
    upload_to = 'GlintNews/HumanArticles/ThumbNail'
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(upload_to, filename)

class ArticleCategory(Model):
    name = models.TextField(_('카테고리명'), unique=True)

    class Meta:
        verbose_name = verbose_name_plural = _('기사 카테고리')
        db_table = 'article_categories'
        ordering = ['-created']

    def __str__(self):
        return self.name


class ArticleTag(Model):
    name = models.TextField(_('태그명'), unique=True)

    class Meta:
        verbose_name = verbose_name_plural = _('기사 태그')
        db_table = 'article_tags'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Article(Model,
              ArticleModelMixin
              ):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='articles',
                                 verbose_name=_('기사 카테고리'))
    tags = models.ManyToManyField(ArticleTag, related_name='articles', verbose_name=_('기사 태그'))
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='articles', verbose_name=_('글쓴이'))

    class Meta:
        verbose_name = verbose_name_plural = _('기사')
        db_table = 'articles'
        ordering = ['-created']


class HumanArticle(Model,
                   ArticleModelMixin
                   ):
    name = models.TextField(_('인물 이름'), blank=True, null=True)
    class Meta:
        verbose_name = verbose_name_plural = _('인물 기사')
        db_table = 'human_articles'
        ordering = ['-created']


class Episode(Model):

    number = models.PositiveIntegerField(_('에피소드 넘버'))
    name = models.TextField(_('에피소드 명'), unique=True)
    subtitle = models.TextField(_('부제목'), blank=True, null=True)
    content = models.TextField(_('에피소드 내용'), blank=True, null=True)
    human_articles = models.ForeignKey(HumanArticle, on_delete=models.CASCADE, related_name='episodes')
    thumbnail = models.ImageField(upload_to=image_path, null=True)

    class Meta:
        verbose_name = verbose_name_plural = _('인물기사 에피소드')
        db_table = 'episodes'
        ordering = ['-created']

    def __str__(self):
        return self.name
