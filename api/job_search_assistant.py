# This API is an experimental prototype for Project Proposal 2 (LLM job search)
# Recommended endpoint: /api/greeting

import logging


logger = logging.getLogger(__name__)


def get_greeting():
    return {'content': "Hello, I am Deep Thought. I am an here to help you.", 'debug': "hardcoded"}


opening_instructions_html = """<p> Describe to me what kind of jobs are you looking for... Are you interested in a 
certain profession? Provide details like: full time job or part time, what experience level, which location. Provide 
as many details as you want, and speak freely. </p>

<p>
I will interpret what you said with help of AI and recommend you occupations that might be of interest to you.
"""


# Recommended endpoint: /api/opening_instructions
def get_opening_instructions():
    return {'content': opening_instructions_html, 'debug': "hardcoded"}


llm_si = """Imagine you are a job counselor. You task is to help a job seeker find a job that is well suited for 
their interests and skill level. You encourage people to find jobs that make sense, e.g. they have a positive impact 
on the environment or on society."""


llm_prompt_tmpl1 = """Given the following input form a job seeker, what kind of jobs would you recommend to the job 
seeker. Please give your answer as a list, one recommendation per line.

User input: {user_input}

Please give your answer in json format. Each recommendation should have two fields: JOB TITLE, DESCRIPTION."""


def generate(user_input: str):
    # TODO: vertexai
    # vertexai.init(project="jobs-that-makesense-dev", location="us-central1")
    # model = GenerativeModel(
    #     "gemini-1.5-flash-001",
    #     system_instruction=[llm_si]
    # )
    # responses = model.generate_content(
    #     [llm_prompt_tmpl1.fomat(user_input=user_input)],
    #     generation_config=generation_config,
    #     safety_settings=safety_settings,
    #     stream=True,
    # )

    return {'content': "OK", 'meta': {'debug': "hardcoded"}}


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    # TODO: vertexai
    # generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    # generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    # generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    # generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


# Recommended endpoint: '/api/send_message'
def process_user_message(user_input: str):
    logger.debug("Processing user message...")
    generate(user_input)
    return {'content': "WIP", 'debug': "WIP"}
