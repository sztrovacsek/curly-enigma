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


# TODO: remove this temporary endpoint
@app.route('/api/candidate_info_instant', methods=['POST'])
def submit_and_process_candidate_info():
    try:
        data = request.get_json()
        userid = data.get('userid')
        occupation = data.get('occupations')[0]
        job_matching_service.store_user_info(userid, occupation['description'])
        result = job_matching_service.get_job_suggestions(userid, occupation['description'])
        logger.debug(f"Jobs matched: {result}")
        return jsonify(result)
    except Exception as e:
        logger.debug("Could not process the input: %s", e)
        return jsonify(f"[API error]: {e}")

    return jsonify("[API error]")


@app.route('/api/candidate_info', methods=['POST'])
def submit_candidate_info():
    try:
        data = request.get_json()
        userid = data.get('userid')
        # Get job suggestions based on the free form description of the first occupation
        # Note that this is logic a stub. When fully implemented, it will take the input from all occupations.
        occupation = data.get('occupations')[0]
        result = job_matching_service.store_user_info(userid, occupation['description'])
        return jsonify(result)
    except Exception as e:
        logger.debug("Could not process the input: %s", e)
        return jsonify(f"[API error]: {e}")

    return jsonify("[API error]")


@app.route('/api/job_suggestions', methods=['GET'])
def get_job_suggestions():
    # TODO: get the real user id and remove the job_preferences_nl param
    result = job_matching_service.get_job_suggestions(userid="user42", job_preferences_nl="")
    logger.debug(f"Jobs matched: {result}")
    return jsonify(result)

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
