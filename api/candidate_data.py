import logging
import time


logger = logging.getLogger(__name__)


# Recommended endpoint: /api/candidate_info (POST request)
def store_candidate_info(userid: str, data: dict):
    # TODO: save the data for this user (to the storage)
    return {'content': 'OK',
            'meta': {
                'reply_to': userid,
                'debug': "Data will be persisted on this request. (In this version: it's not persisted.)"
            }}