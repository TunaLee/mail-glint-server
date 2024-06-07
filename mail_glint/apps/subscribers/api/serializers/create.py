# Serializers
from mail_glint.bases.api.serializers import ModelSerializer

# Models
from mail_glint.apps.subscribers.models.index import Subscriber, SubscriberAuthentication


# Class Section
class SubscriberCreateSerializer(ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email', 'language')

class SubscriberAuthenticationSerializer(ModelSerializer):

    class Meta:
        model = SubscriberAuthentication
        fields = ('email',)
