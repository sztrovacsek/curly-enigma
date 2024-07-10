import logging

from flask import Flask, jsonify, render_template
from datetime import datetime

from api import api


logger = logging.getLogger(__name__)


app = Flask(__name__)


def render_index():
    return render_template('index.html', last_update_time="Jul 10",
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/')
def index():
    return render_index()


@app.route('/api/greeting', methods=['GET'])
def greeting():
    return jsonify(api.get_greeting())


@app.route('/api/opening_instructions', methods=['GET'])
def opening_instructions():
    return jsonify(api.get_opening_instructions())


if __name__ == '__main__':
    app.run(debug=True)
