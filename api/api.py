opening_instructions_html = """
<p>
Describe to me what kind of jobs are you looking for... Are you interested in a certain profession? Provide details like: full time job or part time, what experience level, which location. Provide as many details as you want, and speak freely. 
</p>

<p>
I will interpret what you said with help of AI and recommend you occupations that might be of interest to you. In a future version, I will recommend you concrete job postings from the makesense.org job portal.
"""


def get_greeting():
    return {'content': "Hello", 'debug': "hardcoded"}


def get_opening_instructions():
    return {'content': opening_instructions_html, 'debug': "hardcoded"}
