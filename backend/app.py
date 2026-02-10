# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load data once at startup
brent = pd.read_csv("data/BrentOilPrices.csv", parse_dates=["Date"], dayfirst=True)
events = pd.read_csv("data/oil_events.csv", parse_dates=["Date"], dayfirst=True)

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome! This API serves Brent price and event data.",
        "endpoints":[
            "/api/status",
            "/api/prices",
            "/api/events",
            "/api/change_points"
        ]
    })

@app.route("/api/status")
def status():
    return jsonify({"status": "API is running"})

@app.route("/api/prices")
def get_prices():
    start = request.args.get("start")
    end = request.args.get("end")
    df = brent.copy()
    if start:
        df = df[df.Date >= pd.to_datetime(start)]
    if end:
        df = df[df.Date <= pd.to_datetime(end)]
    return jsonify(df.to_dict(orient="records"))

@app.route("/api/events")
def get_events():
    return jsonify(events.to_dict(orient="records"))

@app.route("/api/change_points")
def change_points():
    cp = {"estimated_date": "2022-02-24", "mu_before": 60, "mu_after": 95}
    return jsonify(cp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
