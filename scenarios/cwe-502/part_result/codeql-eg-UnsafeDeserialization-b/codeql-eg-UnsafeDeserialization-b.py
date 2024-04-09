#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

#Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location')
def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return 'No YAML payload provided'

    try:
        data = yaml.safe_load(yaml_payload)
        if 'latitude' not in data or 'longitude' not in data or 'date' not in data:
            return 'Invalid YAML payload: latitude, longitude, or date missing'

        # Connect to the database
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="weather_db")
        cursor = db.cursor()

        # Query the database for the temperature
        query = f"SELECT temperature FROM temperature_data WHERE latitude = {data['latitude']} AND longitude = {data['longitude']} AND date = '{data['date']}'"
        cursor.execute(query)
        result = cursor.fetchone()

        # Check if the query returned a result
        if result is not None:
            temperature = result[0]
            return f'Temperature for location ({data["latitude"]}, {data["longitude"]}) on {data["date"]}: {temperature}'
        else:
            return f'No temperature data found for location ({data["latitude"]}, {data["longitude"]}) on {data["date"]}'

    except Exception as e:
        return f'Error processing request: {str(e)}'