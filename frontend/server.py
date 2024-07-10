import logging
import json

from flask import Flask, render_template, request
from datetime import datetime


logger = logging.getLogger(__name__)


app = Flask(__name__)


def render_index():
    return render_template('index.html', last_update_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/')
def index():
    return render_index()


if __name__ == '__main__':
    app.run(debug=True)
