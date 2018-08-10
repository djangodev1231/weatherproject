from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Weather
from .serializers import WeatherSerializer
from .filters import WeatherFilter


class WeatherViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filterset_class = WeatherFilter

    @action(detail=False, methods=['DELETE'])
    def erase(self, request):
        try:
            Weather.objects.all().delete()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

