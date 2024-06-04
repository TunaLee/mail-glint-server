# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

from mail_glint.apps.articles.api.views.index import ArticleViewSet, HumanArticleViewSet
from mail_glint.apps.subscribers.api.views.index import SubscriberViewSet, SubscriberAuthenticationViewSet
# users
from mail_glint.apps.users.api.views import UserViewSet




# Router
router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserViewSet)
router.register("subscribe", SubscriberViewSet)
router.register("article", ArticleViewSet)
router.register("human-article", HumanArticleViewSet)
router.register("authenticated", SubscriberAuthenticationViewSet)

app_name = 'api'
urlpatterns = [
                  path('', include("mail_glint.apps.users.urls")),
              ] + router.urls
