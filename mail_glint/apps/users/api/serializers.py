# Local
from rest_framework.fields import SerializerMethodField

from mail_glint.apps.users.models import User
from mail_glint.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)

class AuthorProfileSerializer(ModelSerializer):
    thumbnailImage = SerializerMethodField()
    class Meta:
        model = User
        fields = ('username', 'description', 'thumbnailImage')

    def get_thumbnailImage(self, obj):
        return obj.thumbnail.url
