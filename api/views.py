from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from .filters import MetricFilter
from .models import Metric
from .serializers import MetricSerializer


class MetricViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = MetricFilter
    ordering_fields = '__all__'
