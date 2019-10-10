import factory
import factory.fuzzy

from api.models import Metric


class MetricFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Metric

    date = factory.Faker('date')
    channel = factory.fuzzy.FuzzyChoice(['facebook', 'google'])
    country = factory.Faker('country_code')
    os = factory.fuzzy.FuzzyChoice(['android', 'ios'])
    impressions = factory.Faker('pyint', min_value=1)
    clicks = factory.Faker('pyint', min_value=1)
    installs = factory.Faker('pyint', min_value=1)
    spend = factory.Faker('pyint', min_value=1)
    revenue = factory.Faker('pyfloat', positive=True)

    @classmethod
    def bulk_create(cls, *items):
        for item in items:
            cls(**item)
