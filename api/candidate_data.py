import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def store_candidate_info(userid: str, data: dict):
    # TODO: save the data for this user (to the storage)
    return {
        'content': 'OK',
        'meta': {
            'reply_to': userid,
            'debug': "Data successfully saved. [Stub]"
        },
    }


skill_list = [
    {
        'skill_name': 'Customer service',
        'related_to': 'Bookseller'
    },
    {
        'skill_name': 'Inventory management',
        'related_to': 'Bookseller'
    },
    {
        'skill_name': 'Communication',
        'related_to': 'Bookseller'
    },
    {
        'skill_name': 'Customer service',
        'related_to': 'Organization'
    },
]


def get_candidate_info(userid: str):
    return {
        'content': {
            'userid': userid,
            'occupations': {
                ''
                'last_updated': datetime.now(),
            },
            'skills': {
                'last_updated': datetime.now(),
                'skill_list': skill_list,
            }
        },
        'meta': {
            'reply_to': userid,
            'debug': "Hardcoded"
        }
}


def get_candidate_skills(userid: str, simplified: bool = True):
    if not simplified:
        return {'content': {
            'skills_list': skill_list,
        }}
    else:
        return {
            'content': {
                'skills_list': [
                    'Customer service',
                    'Inventory management',
                    'Communication',
                    'Customer service',
                ],
            },
            'meta': {
                'reply_to': userid,
                'debug': "Hardcoded"
            }

        }
