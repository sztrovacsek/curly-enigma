import logging

from flask import Flask, jsonify, render_template, request
from datetime import datetime

from api import job_search_assistant
from api import  job_matching_service


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', last_update_time="Jul 17",
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# ---- Endpoints for the API demo below --------------------------------------------------------------------------------


@app.route('/api-demo')
def api_demo_form():
    return render_template('api_demo.html',
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/api/candidate_info_instant', methods=['POST'])
def process_candidate_info():
    try:
        data = request.get_json()
        userid = data.get('userid')
        job_preferences_nl = data.get('job_preferences').get('job_preferences_story')
        job_matching_service.store_user_info(userid, job_preferences_nl)
        result = job_matching_service.get_job_suggestions(userid, job_preferences_nl)
        logger.debug(f"Jobs matched: {result}")
        return jsonify("OK")
    except Exception as e:
        logger.debug("Could not process the input: %s", e)
        return jsonify(f"[API error]: {e}")

    return jsonify("[API error]")


@app.route('/api/candidate_info', methods=['POST'])
def submit_candidate_info():
    try:
        data = request.get_json()
        userid = data.get('userid')
        job_preferences_nl = data.get('job_preferences').get('job_preferences_story')
        result = job_matching_service.store_user_info(userid, job_preferences_nl)
        return jsonify(result)
    except Exception as e:
        logger.debug("Could not process the input: %s", e)
        return jsonify(f"[API error]: {e}")

    return jsonify("[API error]")

# ---- Endpoints for the API demo until here ---------------------------------------------------------------------------


@app.route('/candidate')
def candidate_input_form():
    return render_template('candidate-input.html',
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

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


if __name__ == '__main__':
    app.run(debug=True)
