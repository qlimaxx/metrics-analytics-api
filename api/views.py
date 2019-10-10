from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from .filters import MetricFilter
from .models import Metric
from .serializers import MetricSerializer


class MetricViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MetricSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = MetricFilter
    ordering_fields = '__all__'
    group_by_field = 'groupby'
    aggregation_field = 'fields'
    group_by_fields = ['date', 'channel', 'country', 'os']
    aggregation_fields = ['impressions', 'clicks',
                          'installs', 'spend', 'revenue', 'cpi']

    def get_queryset(self):
        queryset = Metric.objects.all()
        groups = self.request.query_params.get(self.group_by_field)
        if groups:
            queryset = self.perform_groub_by(queryset, groups.split(','))
            aggregations = self.request.query_params.get(
                self.aggregation_field)
            if aggregations:
                queryset = self.perform_aggregations(
                    queryset, aggregations.split(','))
        return queryset

    def perform_groub_by(self, queryset, group_by_fields):
        if group_by_fields:
            fields = []
            for field in group_by_fields:
                if field in self.group_by_fields:
                    fields.append(field)
            if fields:
                queryset = queryset.values(*fields)
        return queryset

    def perform_aggregations(self, queryset, aggregation_fields):
        if aggregation_fields:
            aggregations = {}
            for field in aggregation_fields:
                if field in self.aggregation_fields:
                    if field == 'cpi':
                        aggregations[field] = Sum(
                            'spend')/Cast(Sum('installs'), FloatField())
                    else:
                        aggregations[field] = Sum(field)
            if aggregations:
                queryset = queryset.annotate(**aggregations)
        return queryset
