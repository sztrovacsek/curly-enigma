import logging

from flask import Flask, jsonify, render_template, request
from datetime import datetime

from api import job_search_assistant
from api import  job_matching_service


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    return render_index()


@app.route('/candidate')
def candidate_input():
    return render_candidate_input_form()


@app.route('/search')
def job_search():
    return render_template('job-search.html',
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


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
        x = job_search_assistant.add_user_input(user_input)
        return jsonify(x)

    except Exception as e:
        logger.debug("Could not parse the input: %s", e)

    return jsonify("[API error]")


@app.route('/api/candidate_info', methods=['POST'])
def process_candidate_info():
    try:
        data = request.get_json()
        userid = data.get('userid')
        job_preferences_nl = data.get('job_preferences').get('job_preferences_stroy')
        x = job_matching_service.get_job_suggestions(userid, job_preferences_nl)
        return jsonify(x)

    except Exception as e:
        logger.debug("Could not parse the input: %s", e)

    return jsonify("[API error]")


def render_index():
    return render_template('index.html', last_update_time="Jul 15",
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def render_candidate_input_form():
    return render_template('candidate-input.html',
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    app.run(debug=True)
