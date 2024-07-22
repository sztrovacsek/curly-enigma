import logging

from flask import Flask, jsonify, render_template, request
from datetime import datetime

from api import candidate_data
from api import job_matching_service
from api import skill_identification_service


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', last_update_time="Jul 17",
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/api-demo')
def api_demo_form():
    return render_template('api_demo.html',
                           render_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/api/candidate_info', methods=['POST'])
def post_candidate_info():
    try:
        data = request.get_json()
        userid = data.get('userid')
        occupations = data.get('occupations')
        response = candidate_data.store_candidate_info(userid, occupations)
        return jsonify(response)
    except Exception as e:
        logger.debug("Could not process the input: %s", e)
        return jsonify(f"[API error]: {e}")


@app.route('/api/candidate_info/<userid>', methods=['GET'])
def get_candidate_info(userid: str):
    try:
        response = candidate_data.get_candidate_info(userid)
        return jsonify(response)
    except Exception as e:
        logger.debug("Could not process the input: %s", e)
        return jsonify(f"[API error]: {e}")


@app.route('/api/job_suggestions', methods=['GET'])
def get_job_suggestions():
    # TODO: get the real user id and remove the job_preferences_nl param
    result = job_matching_service.get_job_suggestions(userid="user42", job_preferences_nl="")
    logger.debug(f"Jobs matched: {result}")
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
