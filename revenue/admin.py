from django.contrib import admin
from revenue.models import RevenueStatistic


@admin.register(RevenueStatistic)
class RevenueStatisticAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'revenue']
    search_fields = ['name']

    autocomplete_fields = ['spend']

