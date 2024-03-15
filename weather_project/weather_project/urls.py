
from django.contrib import admin
from django.urls import path , include
from weather_app.views import WeatherView

urlpatterns = [
    path("", WeatherView.as_view(), name="weather"),
    path("admin/", admin.site.urls),
    #path('weather/', include('weather_app.urls')),
]
