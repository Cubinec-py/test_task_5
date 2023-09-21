from django.urls import path, include

from rest_framework.routers import DefaultRouter

from revenue.views import RevenueStatisticViewSet
from spend.views import SpendStatisticViewSet

router = DefaultRouter()

router.register('revenue', RevenueStatisticViewSet, basename='revenue')
router.register('spend', SpendStatisticViewSet, basename='spend')

urlpatterns = [
    path('', include(router.urls)),
]
