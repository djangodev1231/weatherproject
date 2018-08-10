from django_filters import rest_framework as filters

from .models import Weather


class WeatherFilter(filters.FilterSet):
    lon = filters.NumberFilter(field_name="location__lon")
    lat = filters.NumberFilter(field_name="location__lat")
    city = filters.CharFilter(field_name="location__city")
    state = filters.CharFilter(field_name="location__state")
    start_date = filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = Weather
        fields = ['lon', 'lat', 'start_date', 'end_date', 'state', 'city']
