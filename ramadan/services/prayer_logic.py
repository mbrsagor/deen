from datetime import datetime, timedelta
from .bangladesh_ramadan import get_official_ramadan_time, is_eid_day

def build_prayer_response(aladhan_data, district):
    timings = aladhan_data["timings"]
    hijri = aladhan_data["date"]["hijri"]

    hijri_month = int(hijri["month"]["number"])
    hijri_day = int(hijri["day"])

    today = datetime.today().date()

    response = {
        "sunrise": timings["Sunrise"],
        "sunset": timings["Sunset"],
        "five_prayers": {
            "Fajr": timings["Fajr"],
            "Dhuhr": timings["Dhuhr"],
            "Asr": timings["Asr"],
            "Maghrib": timings["Maghrib"],
            "Isha": timings["Isha"],
        },
        "is_ramadan": hijri_month == 9,
        "is_eid": False,
        "sehri_iftar": None,
        "hijri_date": hijri["date"],
        "gregorian_date": aladhan_data["date"]["gregorian"]["date"],
    }

    # Eid handling
    if is_eid_day(today, district):
        response["is_eid"] = True
        response["message"] = "Eid Mubarak! 🌙"
        return response

    # Ramadan Sehri / Iftar
    if hijri_month == 9:
        official = get_official_ramadan_time(today, district)
        if official:
            response["sehri_iftar"] = official

    return response
