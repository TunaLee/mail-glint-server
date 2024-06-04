# Django
import random

from django.core.mail import send_mail
from django.db import transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action

from mail_glint.apps.subscribers.api.serializers.create import SubscriberCreateSerializer, \
    SubscriberAuthenticationSerializer
from mail_glint.apps.subscribers.models.index import Subscriber, SubscriberAuthentication
from mail_glint.apps.users.decorators import verify_email_decorator
# Local
from mail_glint.bases.api import mixins
from mail_glint.bases.api.viewsets import GenericViewSet
from mail_glint.utils.api.response import Response
from mail_glint.utils.decorators import create_decorator
from mail_glint.utils.emails import send_verification_email


# Class Section
class SubscriberViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializers = {
        'default': SubscriberCreateSerializer,
    }
    queryset = Subscriber.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**create_decorator(title=_('구독자 등록')))
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        language = request.data.get('language')
        send_verification_email(code, email)

        authentication, is_created = SubscriberAuthentication.objects.get_or_create(email=email)
        authentication.save()
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok')
        )


class SubscriberAuthenticationViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializers = {
        'default': SubscriberAuthenticationSerializer,
    }
    queryset = Subscriber.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**verify_email_decorator(title=_('구독자 이메일 검증'), serializer=SubscriberAuthenticationSerializer))
    @action(detail=False, methods=['post'])
    def verify_email(self, request, *args, **kwargs):
        code = request.data.get('code')
        email = request.data.get('email')
        authentication = SubscriberAuthentication.objects.get(email=email)
        subscriber = Subscriber.objects.get(email=email)
        serializer = self.get_serializer(data=request.data)
        if timezone.now() > authentication.expires_at:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('expired code')
            )
        if authentication.verify_code == code:
            authentication.is_verified = True
            authentication.save()
            subscriber.is_active = True
            subscriber.save()
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                return Response(
                    status=status.HTTP_201_CREATED,
                    code=201,
                    message=_('ok'),
                    data=serializer.data
                )
