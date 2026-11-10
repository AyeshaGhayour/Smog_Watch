
def classify_air_quality(pm2_5):
    if pm2_5 <= 5:
        return "Good"
    elif pm2_5 <= 15:
        return "Moderate"
    elif pm2_5 <= 35:
        return "Unhealthy for Sensitive Groups"
    elif pm2_5 <= 55:
        return "Unhealthy"
    elif pm2_5 <= 150:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def rank_cities(city_data):
    """Rank cities from lowest to highest PM2.5 concentration."""

    ranked_cities = sorted(
        city_data,
        key=lambda city: city["pm2_5"]
    )

    return ranked_cities
