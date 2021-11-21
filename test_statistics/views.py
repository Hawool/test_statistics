import django_filters
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from test_statistics.models import StatisticModel
from test_statistics.serializers import StatisticModelSerializer, StatisticModelCreateSerializer


class SerializerByMethodMixin:
    """choosing serializer for method"""
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class StatisticsFilter(django_filters.FilterSet):
    class Meta:
        model = StatisticModel
        fields = {
            'views': ['lte', 'gte'],
            'clicks': ['lte', 'gte'],
            'cost': ['lte', 'gte'],
            'date': ['lte', 'gte'],
        }


class StatisticModelViewSet(SerializerByMethodMixin, ModelViewSet):
    queryset = StatisticModel.objects.annotate(cpc=F('cost')/F('clicks'), cpm=F('cost')/F('views')*1000)
    serializer_map = {
        'GET': StatisticModelSerializer,
        'POST': StatisticModelCreateSerializer,
        'PUT': StatisticModelCreateSerializer,
        'PATCH': StatisticModelCreateSerializer,
        'DELETE': StatisticModelCreateSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_class = StatisticsFilter
