import logging
from datetime import datetime

logger = logging.getLogger(__name__)


# Recommended endpoint: /api/candidate_info (POST request)
def store_candidate_info(userid: str, data: dict):
    # TODO: save the data for this user (to the storage)
    return {'content': 'OK',
            'meta': {
                'reply_to': userid,
                'debug': "Data successfully saved. [Stub: not persisted]"
            }}


# Recommended endpoint: /api/candidate_info (GET request)
def get_candidate_info(userid: str):
    return {'content': {
        'userid': userid,
        'occupations': {
            'last_updated': datetime.now(),
        },
        'skills': {
            'last_updated': datetime.now(),
            'skill_list': ['sales', 'marketing', 'customer service'],
        }
    }
}
