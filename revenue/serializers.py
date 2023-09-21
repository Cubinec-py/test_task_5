from rest_framework import serializers
from django.db.models import Sum
from revenue.models import RevenueStatistic


class RevenueStatisticSerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, coerce_to_string=False)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    total_clicks = serializers.IntegerField()
    total_impressions = serializers.IntegerField()
    total_conversion = serializers.IntegerField()

    @classmethod
    def get_queryset(cls):
        queryset = RevenueStatistic.objects.values('date', 'name').annotate(
            total_revenue=Sum('revenue'),
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        ).order_by('date')

        return queryset


