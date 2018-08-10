from rest_framework import serializers

from .models import Location, Weather


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('lat', 'lon', 'city', 'state', )


class WeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=True)

    class Meta:
        model = Weather
        fields = ('id', 'date', 'temperature', 'location', )

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        weather = Weather.objects.create(location=location, **validated_data)
        return weather

