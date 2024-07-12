import logging

from flask import Flask, jsonify, render_template, request
from datetime import datetime

from api import job_search_assistant


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
    return jsonify(job_search_assistant.get_greeting())


@app.route('/api/opening_instructions', methods=['GET'])
def opening_instructions():
    return jsonify(job_search_assistant.get_opening_instructions())


@app.route('/api/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        user_input = data.get('user_input')
        return jsonify(job_search_assistant.process_user_message(user_input))

    except Exception as e:
        logger.debug("Could not parse the input: %s", e)

    return jsonify("[API error]")


if __name__ == '__main__':
    app.run(debug=True)
