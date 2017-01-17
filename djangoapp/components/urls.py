from django.conf.urls import url, include
from rest_framework import routers

from djangoapp.components import views

router = routers.DefaultRouter()
router.register(r'processors', views.ProcessorViewSet)

app_name = 'components'
urlpatterns = [
    url(r'^', include(router.urls)),
]
