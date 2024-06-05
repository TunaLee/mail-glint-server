# Serializers
from rest_framework.fields import SerializerMethodField

# Models
from mail_glint.apps.articles.models.index import Article, ArticleTag, HumanArticle, Episode
from mail_glint.apps.users.api.serializers import AuthorProfileSerializer
from mail_glint.bases.api.serializers import ModelSerializer


# Class Section
class ArticleRetrieveSerializer(ModelSerializer):
    tags = SerializerMethodField()
    thumbnailImage = SerializerMethodField()
    authorProfile = AuthorProfileSerializer(read_only=True, source='author')

    class Meta:
        model = Article
        fields = ('id', 'title', 'subtitle', 'tags', 'authorProfile', 'category', 'created', 'content', 'likes', 'views',
                  'thumbnailImage')

    def get_tags(self, obj):
        return [tag.name for tag in ArticleTag.objects.filter(articles=obj)]

    def get_thumbnailImage(self, obj):
        return obj.thumbnail.url



class EpisodeSerializer(ModelSerializer):
    class Meta:
        model = Episode
        fields = ('number', 'name', 'thumbnail', 'content', 'subtitle')


class HumanArticleRetrieveSerializer(ModelSerializer):
    episodes = SerializerMethodField()
    thumbnailImage = SerializerMethodField()

    class Meta:
        model = HumanArticle
        fields = ('id', 'title', 'subtitle', 'name', 'episodes', 'created', 'likes', 'views', 'thumbnailImage')

    def get_thumbnailImage(self, obj):
        return obj.thumbnail.url

    def get_episodes(self, obj):
        episodes = obj.episodes.all().order_by('number')
        return EpisodeSerializer(episodes, many=True).data
