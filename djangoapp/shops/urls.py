from django.conf.urls import url, include
from rest_framework import routers

from djangoapp.shops import views

router = routers.DefaultRouter()
router.register(r'', views.SaleViewSet)

app_name = 'sales'
urlpatterns = [
    url(r'^', include(router.urls)),
]
