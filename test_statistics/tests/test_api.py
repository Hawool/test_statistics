from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from test_statistics.models import StatisticModel
from test_statistics.serializers import StatisticModelCreateSerializer


class StatisticModelTestCase(APITestCase):
    """testing methods: get, post, put, delete"""

    def setUp(self):
        self.stat_1 = StatisticModel.objects.create(date='2021-11-12', views=32, clicks=100, cost=120)
        self.stat_2 = StatisticModel.objects.create(date='2021-11-25', views=2, clicks=10, cost=1120)
        self.data = {"date": "2021-11-12",
                     "views": 32,
                     "clicks": 100,
                     "cost": "120.00"}
        self.wrong_data = {"date": "2021-11-12",
                           "views": 'tgt',
                           "clicks": 100,
                           "cost": "120.00"}

    def test_can_create_statisticmodel(self):
        url = reverse('statisticmodel-list')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_statisticmodel(self):
        url = reverse('statisticmodel-list')
        response = self.client.post(url, self.wrong_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_read_statisticmodel_list(self):
        response = self.client.get(reverse('statisticmodel-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_statisticmodel_detail(self):
        response = self.client.get(reverse('statisticmodel-detail', args=[self.stat_1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_read_statisticmodel_detail(self):
        response = self.client.get(reverse('statisticmodel-detail', args=[20]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_statisticmodel(self):
        self.data = StatisticModelCreateSerializer(self.stat_1).data
        self.data.update({'views': 10000})
        response = self.client.put(reverse('statisticmodel-detail', args=[self.stat_1.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_statisticmodel(self):
        response = self.client.delete(reverse('statisticmodel-detail', args=[self.stat_1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
