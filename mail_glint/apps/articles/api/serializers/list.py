# Serializers
from rest_framework.fields import SerializerMethodField

from mail_glint.apps.articles.api.serializers.retreive import EpisodeSerializer
from mail_glint.apps.articles.models.index import Article, ArticleTag, HumanArticle
from mail_glint.apps.users.api.serializers import AuthorProfileSerializer
from mail_glint.bases.api.serializers import ModelSerializer


# Models


# Class Section

class ArticleListSerializer(ModelSerializer):
    tags = SerializerMethodField()
    thumbnailImage = SerializerMethodField()
    authorName = SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'tags', 'authorName', 'subtitle', 'created', 'likes', 'views', 'thumbnailImage')

    def get_tags(self, obj):
        return [tag.name for tag in ArticleTag.objects.filter(articles=obj)]

    def get_thumbnailImage(self, obj):
        return obj.thumbnail.url

    def get_authorName(self, obj):
        return obj.author.username


class HumanArticleListSerializer(ModelSerializer):
    thumbnailImage = SerializerMethodField()
    episodes = SerializerMethodField()

    class Meta:
        model = HumanArticle
        fields = ('id', 'episodes', 'name', 'title', 'subtitle', 'created', 'likes', 'views', 'thumbnailImage')

    def get_thumbnailImage(self, obj):
        return obj.thumbnail.url

    def get_episodes(self, obj):
        episodes = obj.episodes.all().order_by('number')
        return EpisodeSerializer(episodes, many=True).data
