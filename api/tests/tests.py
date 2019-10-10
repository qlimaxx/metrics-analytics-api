from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import MetricFactory


class MetricViewSetTestCase(APITestCase):

    def test_filtering(self):
        MetricFactory.bulk_create({'country': 'US'}, {'country': 'DE'})
        response = self.client.get(
            reverse('api:metrics-list'), {'country': 'US'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_sorting(self):
        dates = [{'date': '2019-10-01'},
                 {'date': '2019-10-03'},
                 {'date': '2019-10-02'}]
        MetricFactory.bulk_create(*dates)
        response = self.client.get(
            reverse('api:metrics-list'), {'ordering': '-date'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_dates = [{'date': item['date']}for item in response.json()]
        sorted_dates = sorted(dates, key=lambda e: e['date'], reverse=True)
        self.assertEqual(response_dates, sorted_dates)

    def test_group_by(self):
        MetricFactory.bulk_create(
            {'country': 'US'}, {'country': 'US'},
            {'country': 'DE'}, {'country': 'DE'})
        response = self.client.get(
            reverse('api:metrics-list'), {'groupby': 'country',
                                          'fields': 'clicks,country'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_aggregation(self):
        MetricFactory.bulk_create(
            {'impressions': 2, 'clicks': 1, 'country': 'US'},
            {'impressions': 2, 'clicks': 2, 'country': 'US'})
        response = self.client.get(
            reverse('api:metrics-list'), {'groupby': 'country',
                                          'fields': 'impressions,clicks,country'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['clicks'], 3)
        self.assertEqual(response.json()[0]['impressions'], 4)

    def test_cpi(self):
        MetricFactory.bulk_create(
            {'spend': 2.5, 'installs': 1, 'country': 'US'},
            {'spend': 3.5, 'installs': 2, 'country': 'US'})
        response = self.client.get(
            reverse('api:metrics-list'), {'groupby': 'country',
                                          'fields': 'cpi,country'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['cpi'], 2)
