from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ramadan.services.aladhan import fetch_prayer_data
from ramadan.services.prayer_logic import build_prayer_response


class PrayerAPIView(APIView):
    """
    This API is used to get prayer times for a specific city.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        city = request.query_params.get("city", "Dhaka")
        district = request.query_params.get("district", "Dhaka")

        aladhan_data = fetch_prayer_data(city)
        data = build_prayer_response(aladhan_data, district)

        return Response({
            "status": "success",
            "message": "Data returned successfully.",
            "data": data
        })
