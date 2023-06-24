
from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

weather_key = os.environ.get("WEATHER_KEY")


@proxy_bp.route("/weather", methods=["GET"])
def get_weather():
    city_query = request.args.get("q")
    print(city_query)
    if not city_query:
        return {"message": "must provide city parameters"}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city_query,  "appid": weather_key}
    )
    return response.json()
