# This code is not ready to use. It is just an example json api implementation.

import logging
import json

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


logger = logging.getLogger(__name__)


app = Flask(__name__)


# Load Data (Simulating a Database)
with open('data.json', 'r') as f:
    data = json.load(f)


# Endpoints
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404


@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = max(item['id'] for item in data) + 1
    data.append(new_item)
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return jsonify(new_item), 201


@app.route('/api/job_', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = max(item['id'] for item in data) + 1
    data.append(new_item)
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return jsonify(new_item), 201


if __name__ == '__main__':
    app.run(debug=True)
