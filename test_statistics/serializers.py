from rest_framework import serializers

from test_statistics.models import StatisticModel


class StatisticModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticModel
        fields = ['views', 'clicks', 'cost', 'date']


class StatisticModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticModel
        fields = '__all__'

    cpc = serializers.DecimalField(max_digits=10, decimal_places=2)
    cpm = serializers.DecimalField(max_digits=10, decimal_places=2)
