from flask import Blueprint, render_template
from app.api import fetch_all_cities
from app.utils import rank_cities

main = Blueprint("main", __name__)

@main.route("/")
def home():
    # Fetch live air quality data
    city_data = fetch_all_cities()

    # Rank cities from lowest to highest PM2.5
    ranked_cities = rank_cities(city_data)

    # Send data to the webpage
    return render_template(
        "smog_watch.html",
        cities=ranked_cities
    )
