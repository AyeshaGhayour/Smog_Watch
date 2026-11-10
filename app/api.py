
from app.utils import classify_air_quality
import requests

# Open-Meteo Air Quality API
API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

# Cities and their geographical coordinates
CITIES = {
    "Karachi": {"latitude": 24.8607, "longitude": 67.0011},
    "Lahore": {"latitude": 31.5204, "longitude": 74.3587},
    "Islamabad": {"latitude": 33.6844, "longitude": 73.0479},
    "Peshawar": {"latitude": 34.0151, "longitude": 71.5249},
    "Quetta": {"latitude": 30.1798, "longitude": 66.9750}
}


def fetch_city_data(city, coordinates):
    """Fetch current PM2.5 data for one city."""

    params = {
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "current": "pm2_5",
        "timezone": "auto"
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()
        current_data = data["current"]

        return {
            "city": city,
            "pm2_5": current_data["pm2_5"],
            "air_quality": classify_air_quality(
                current_data["pm2_5"]
            ),
            "time": current_data["time"],
            "unit": data["current_units"]["pm2_5"]
        }

    except requests.exceptions.RequestException as error:
        print(f"API request failed for {city}: {error}")

    except (KeyError, TypeError) as error:
        print(f"Invalid API response for {city}: {error}")

    return None


def fetch_all_cities():
    """Fetch air quality data for all five cities."""

    results = []

    for city, coordinates in CITIES.items():
        print(f"Fetching data for {city}...")

        city_data = fetch_city_data(city, coordinates)

        if city_data is not None:
            results.append(city_data)

    return results


# Test the API integration
if __name__ == "__main__":
    air_quality_data = fetch_all_cities()

    print("\n===== SMOGWATCH LIVE AIR QUALITY =====")

    for city in air_quality_data:
        print(
            f"{city['city']}: "
            f"{city['pm2_5']} {city['unit']} "
            f"| Category: {city['air_quality']} "
            f"| Updated: {city['time']}"
        )
