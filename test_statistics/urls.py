from django.urls import path, include
from rest_framework import routers
from test_statistics.views import StatisticModelViewSet

router = routers.DefaultRouter()
router.register(r'statistic', StatisticModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]