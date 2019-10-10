from rest_framework import routers

from .views import MetricViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'metrics', MetricViewSet, basename='metrics')

urlpatterns = router.urls
