from unittest import TestCase

from test_statistics.models import StatisticModel
from test_statistics.serializers import StatisticModelCreateSerializer


class StatisticModelSerializerTestCase(TestCase):
    def test_StatisticModelSerializer(self):
        stat_1 = StatisticModel.objects.create(date='2021-11-12', views=32, clicks=100, cost=120)
        stat_2 = StatisticModel.objects.create(date='2021-11-25', views=2, clicks=10, cost=1120)
        data = StatisticModelCreateSerializer([stat_1, stat_2], many=True).data
        expected_data = [
            {
                "date": "2021-11-12",
                "views": 32,
                "clicks": 100,
                "cost": "120.00"
            },
            {
                "date": "2021-11-25",
                "views": 2,
                "clicks": 10,
                "cost": "1120.00"
            },
        ]
        self.assertEqual(expected_data, data)
