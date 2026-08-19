"""Docstring here"""

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Docstring"""
    return {"message": "Hello World"}


@app.post("/convert/{state}/{city}")
def convert(state, city):
    """Docstring here"""
    api_key = "6a85c7cfa8bbb745747450mog493b27"

    payload = {"api_key": api_key, "state": state, "city": city}

    response = requests.get(
        "https://geocode.maps.co/search", params=payload, timeout=100
    )

    best_result = response.json()[0]
    lat = best_result["lat"]
    long = best_result["lon"]
    return {"lat": lat, "long": long}


@app.get("/weather/{lat}/{long}")
def weather(lat, long):
    """Docstring"""
    payload = {"latitude": float(lat), "longitude": float(long)}
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast", params=payload, timeout=100
    )
    return response.json()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
