from rest_framework import serializers
from django.db.models import Sum, Subquery, OuterRef
from spend.models import SpendStatistic
from revenue.models import RevenueStatistic


class SpendStatisticSerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, coerce_to_string=False)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    total_clicks = serializers.IntegerField()
    total_impressions = serializers.IntegerField()
    total_conversion = serializers.IntegerField()

    @classmethod
    def get_queryset(clas):
        subquery = RevenueStatistic.objects.filter(spend_id=OuterRef('pk')).values('spend_id').annotate(
            total_revenue=Sum('revenue'),
        ).values('total_revenue')
        queryset = SpendStatistic.objects.values('date', 'name').annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            total_revenue=Subquery(subquery),
        ).order_by('date')

        return queryset
