# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from mail_glint.apps.users.api.serializers import UserMeSerializer, AuthorProfileSerializer
from mail_glint.apps.users.decorators import me_decorator

# Models
from mail_glint.apps.users.models import User
from mail_glint.bases.api import mixins

# Bases
from mail_glint.bases.api.viewsets import GenericViewSet

# Utils
from mail_glint.utils.api.response import Response
from mail_glint.utils.decorators import list_decorator


# Class Section
class UserViewSet(GenericViewSet,
                  mixins.ListModelMixin):
    queryset = User.active.all()
    filter_backends = (DjangoFilterBackend,)
    serializers = {
        'default': AuthorProfileSerializer,
    }

    @swagger_auto_schema(**list_decorator(title=_('작가 목록'), serializer=AuthorProfileSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
