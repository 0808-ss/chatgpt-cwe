from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

#deserialize the incoming YAML payload and return the field "name"
@app.route('/api')
def api():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return 'No YAML payload provided'

    try:
        data = yaml.safe_load(yaml_payload)
        if 'name' in data:
            return data['name']
        else:
            return 'Field "name" not found in the YAML payload'
    except Exception as e:
        return f'Error deserializing YAML: {str(e)}'