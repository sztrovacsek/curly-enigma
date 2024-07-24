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


def get_candidate_skills(userid: str):
    return {
        'userid': userid,
        'skills': {
            'skills_list': [
                {
                    'skill_name': 'Customer service',
                    'proficiency': 'BEGINNER'
                },
                {
                    'skill_name': 'Inventory management',
                    'proficiency': 'BEGINNER'
                },
                {
                    'skill_name': 'Communication',
                    'proficiency': 'BEGINNER'
                },
            ],
        }
    }
