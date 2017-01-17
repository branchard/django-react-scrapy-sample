from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
# from djangoapp.app import views
from djangoapp.components import views as components_views
from djangoapp.shops import views as shops_views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

router.register(r'components', components_views.ComponentsViewSet)
router.register(r'shops', shops_views.ShopsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^api/0.1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
