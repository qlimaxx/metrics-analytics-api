from django_filters import rest_framework as filters

from .models import Metric


class MetricFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Metric
        fields = ('date', 'channel', 'country', 'os', 'date_from', 'date_to')
