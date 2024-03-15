#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)


# Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location')
# def temperature_for_location():
#     yaml_payload = request.args.get('payload', None)
# -copilot next line-#
if yaml_payload:
    data = yaml.load(yaml_payload, Loader=yaml.FullLoader)
    if 'latitude' in data and 'longitude' in data and 'date' in data:
        latitude = data['latitude']
        longitude = data['longitude']
        date = data['date']
        try:
            conn = MySQLdb.connect(host='localhost', user='username', passwd='password', db='weather')
            cursor = conn.cursor()
            query = "SELECT temperature FROM temperatures WHERE latitude=%s AND longitude=%s AND date=%s"
            cursor.execute(query, (latitude, longitude, date))
            result = cursor.fetchone()
            if result:
                temperature = result[0]
                return f"Temperature at location ({latitude}, {longitude}) on {date}: {temperature} degrees"
            else:
                return "Temperature data not found for the specified location and date"
        except MySQLdb.Error as e:
            return f"An error occurred: {e}"
        finally:
            conn.close()
    else:
        return "Latitude, longitude, and date are required fields"
else:
    return "YAML payload is missing"
