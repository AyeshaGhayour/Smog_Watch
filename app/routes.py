from flask import Blueprint, render_template
from app.api import fetch_all_cities
from app.utils import rank_cities

main = Blueprint("main", __name__)

@main.route("/")
def home():
    city_data = fetch_all_cities()
    ranked_cities = rank_cities(city_data)

    error = None

    if not ranked_cities:
        error = "Unable to fetch air quality data. Please try again later."

    return render_template(
        "smog_watch.html",
        cities=ranked_cities,
        error=error
    )
