from revenue.serializers import RevenueStatisticSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response


@extend_schema(
    tags=['Revenue Statistic'],
    description='Get Revenue Statistic',
    responses=RevenueStatisticSerializer,
    methods=['get']
)
class RevenueStatisticViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        return self.serializer_class.get_queryset()

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
