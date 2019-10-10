from rest_framework import serializers

from .models import Metric


class MetricSerializer(serializers.ModelSerializer):
    cpi = serializers.FloatField()

    class Meta:
        model = Metric
        exclude = ('id',)
