from rest_framework import serializers

from .models import Metric


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that uses `fields` query parameter from request
    to controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('fields')
        if fields:
            # Drop any fields that are not specified in the `fields`.
            allowed = set(fields.split(','))
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MetricSerializer(DynamicFieldsModelSerializer):
    cpi = serializers.FloatField()

    class Meta:
        model = Metric
        exclude = ('id',)
