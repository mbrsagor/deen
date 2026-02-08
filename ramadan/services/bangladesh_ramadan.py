from datetime import date

RAMADAN_TIME = {
    "2026": {
        "Dhaka": {
            "2026-02-18": {"sehri": "05:06", "iftar": "17:59"},
            "2026-02-19": {"sehri": "05:05", "iftar": "18:00"},
        },
        "eid": "2026-03-20"
    }
}

def get_official_ramadan_time(today, district):
    year = str(today.year)
    if year not in RAMADAN_TIME:
        return None

    date_key = today.strftime("%Y-%m-%d")
    return RAMADAN_TIME[year].get(district, {}).get(date_key)


def is_eid_day(today, district):
    year = str(today.year)
    eid_date = RAMADAN_TIME.get(year, {}).get("eid")
    return eid_date == today.strftime("%Y-%m-%d")
