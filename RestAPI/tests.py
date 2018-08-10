from django.urls import include, path, reverse

from rest_framework.routers import DefaultRouter
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

from RestAPI import views


class WeatherTests(APITestCase, URLPatternsTestCase):

    router = DefaultRouter()
    router.register(r'weather', views.WeatherViewSet)

    urlpatterns = [
        path(r'', include(router.urls))
    ]

    def test_weather(self):
        """
        Create Weather test
        """
        url = reverse('weather-list')
        response = self.client.post(url, {"id": 1, "date": "1985-04-16", "location": {"lat": 36.1189, "lon": -86.6892, "city": "Jenkintown", "state": "Pensilvania"}, "temperature": [37.3, 36.8, 36.4, 36.0, 35.6, 35.3, 35.0, 34.9, 35.8, 38.0, 40.2, 42.3, 43.8, 44.9, 45.5, 45.7, 44.9, 43.0, 41.7, 40.8, 39.9, 39.2, 38.6, 38.1]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(url, {"id": 2, "date": "1985-05-21", "location": {"lat": 37.2389, "lon": -56.6712, "city": "New Orleans", "state": "Pensilvania"}, "temperature": [37.3, 36.8, 36.4, 36.0, 35.6, 35.3, 35.0, 34.9, 35.8, 38.0, 40.2, 42.3, 43.8, 44.9, 45.5, 45.7, 44.9, 43.0, 41.7, 40.8, 39.9, 39.2, 38.6, 38.1]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(url, {"id": 3, "date": "1985-04-25", "location": {"lat": 40.5611, "lon": -34.1232, "city": "Atlanta", "state": "Georgia"}, "temperature": [37.3, 36.8, 36.4, 36.0, 35.6, 35.3, 35.0, 34.9, 35.8, 38.0, 40.2, 42.3, 43.8, 44.9, 45.5, 45.7, 44.9, 43.0, 41.7, 40.8, 39.9, 39.2, 38.6, 38.1]},format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Have Same ID
        response = self.client.post(url, {"id": 3, "date": "1985-05-09", "location": {"lat": 21.3243, "lon": -54.3761, "city": "New York", "state": "Washington"}, "temperature": [37.3, 36.8, 36.4, 36.0, 35.6, 35.3, 35.0, 34.9, 35.8, 38.0, 40.2, 42.3, 43.8, 44.9, 45.5, 45.7, 44.9, 43.0, 41.7, 40.8, 39.9, 39.2, 38.6, 38.1]},format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Have Same Date
        response = self.client.post(url, {"id": 4, "date": "1985-04-16", "location": {"lat": 21.3243, "lon": -54.3761, "city": "New York", "state": "Washington"}, "temperature": [37.3, 36.8, 36.4, 36.0, 35.6, 35.3, 35.0, 34.9, 35.8, 38.0, 40.2, 42.3, 43.8, 44.9, 45.5,45.7, 44.9, 43.0, 41.7, 40.8, 39.9, 39.2, 38.6, 38.1]},format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        """
        Get Weather list
        """
        url = reverse('weather-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """
        Get Weather by filter test
        """
        # Test start date / end date filter
        url = reverse('weather-list') + '?start_date=1985-01-01&end_date=1985-04-25'
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test longtude / latitude filter
        url = reverse('weather-list') + '?lat=37.2389&lon=-56.6712'
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test city / state filter
        url = reverse('weather-list') + '?state=Pensilvania'
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('weather-list') + '?city=Jenkintown'
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        """
        Delete Individual Weather test
        """
        url = reverse('weather-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        """
        Delete All Weather test
        """
        url = reverse('weather-list') + 'erase/'
        print(url)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


