from django.conf.urls import url, include

#  now we are using default router for viewset
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

# register our HelloViewSet
router.register('tokenizer', views.TokenizerViewSet, base_name='tokenizer')


urlpatterns = [

    url(r'', include(router.urls)),
]