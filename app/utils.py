
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
