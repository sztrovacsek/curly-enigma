import logging
import time


logger = logging.getLogger(__name__)


# Hardcoded list of suggestions (will be removed in the productionized code).
def job_suggestions():
    suggestions = [
        {
            "job_title": "Cultural Event Assistant",
            "job_description": "Assist in organizing and executing cultural events, such as art exhibitions, concerts, "
                           "or theater performances. This role involves tasks like ticketing, coordinating "
                           "volunteers, and providing logistical support.",
            "link": "https://jobs.makesense.org/en/jobs/delta-france-association-stage-assistante-relations-institutionnelles-culture-HLD7D9ws3Sd0sQUlbqqQ?"
        },
        {
            "job_title": "Tour Guide",
            "job_description": "Lead tours for tourists and visitors, providing information and insights about the "
                           "history, art, and culture of Paris. Requires strong communication skills and knowledge of"
                           " the city.",
            "link": "https://jobs.makesense.org/en/jobs/delta-france-association-stage-assistante-relations-institutionnelles-culture-HLD7D9ws3Sd0sQUlbqqQ?"
        },
    ]
    return suggestions


# Recommended endpoint: /api/job_suggestions (GET request)
def get_job_suggestions(userid: str):
    # TODO: get the data for this user (from the storage)
    # TODO: perform the job matching for real (in this version: it is hardcoded)
    time.sleep(0.5)
    return {
        'content': job_suggestions(),
        'meta': {
            'reply_to': userid,
            'debug': "Hardcoded"
        },
    }
