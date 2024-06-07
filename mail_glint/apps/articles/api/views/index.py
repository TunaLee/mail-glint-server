# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter

from mail_glint.apps.articles.api.serializers.list import ArticleListSerializer, HumanArticleListSerializer
from mail_glint.apps.articles.api.serializers.retreive import ArticleRetrieveSerializer, HumanArticleRetrieveSerializer
from mail_glint.apps.articles.api.views.filters.article_filter import ArticlesFilter
from mail_glint.apps.articles.models.index import Article, ArticleCategory, HumanArticle
from mail_glint.bases.api import mixins
from mail_glint.bases.api.viewsets import GenericViewSet
from mail_glint.utils.decorators import retrieve_decorator, list_decorator


# Local


# Class Section
class ArticleViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet
                     ):
    serializers = {
        'default': ArticleRetrieveSerializer,
        'list': ArticleListSerializer,
    }
    queryset = Article.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['-views', '-likes']
    filterset_class = ArticlesFilter
    @swagger_auto_schema(**retrieve_decorator(title=_('기사 상세'), serializer=ArticleRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(**list_decorator(title=_('기사 목록'), serializer=ArticleListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)



class HumanArticleViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet
                          ):
    serializers = {
        'default': HumanArticleRetrieveSerializer,
        'list': HumanArticleListSerializer,
    }
    queryset = HumanArticle.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['-created']
    # filterset_class = HumanArticlesFilter
    @swagger_auto_schema(**retrieve_decorator(title=_('인물 기사 상세'), serializer=HumanArticleRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(**list_decorator(title=_('인물 기사 목록'), serializer=HumanArticleListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
