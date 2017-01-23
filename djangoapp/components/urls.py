from django.conf.urls import url, include
from rest_framework import routers

from djangoapp.components import views

router = routers.DefaultRouter()
router.register(r'processors', views.ProcessorViewSet)
router.register(r'motherboards', views.MotherboardViewSet)
router.register(r'rams', views.RamViewSet)
router.register(r'cases', views.CaseViewSet)
router.register(r'graphiccards', views.GraphicCardViewSet)
router.register(r'harddrives', views.HardDriveViewSet)
router.register(r'powersupplies', views.PowerSupplyViewSet)

app_name = 'components'
urlpatterns = [
    url(r'^', include(router.urls)),
]
