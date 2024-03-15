from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

class WeatherView(APIView):
    template_name = 'weather.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        city = request.data.get('city', None)
        print("Received city:", city)
        if city:
            response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=1fd75aa8a2f948fabd0114330241403&q={city}')
            
            if response.status_code == 200:
                weather_data = response.json()
                return Response(weather_data)
            else:
                return Response({'error': 'Failed to fetch weather data'}, status=response.status_code)
        else:
            return Response({'error': 'City not provided'}, status=400)
