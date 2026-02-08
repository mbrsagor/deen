from django.urls import path
from ramadan.api.prayer_api import PrayerAPIView


urlpatterns = [
    path("prayer/", PrayerAPIView.as_view(), name="prayer"),
]
