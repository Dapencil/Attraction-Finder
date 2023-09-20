from langchain import PromptTemplate

def get_extract_prompt(user_msg):
    # Extract specification
    template = """{user_msg}
    From the above, Extract information in short and clear include
    place: Where do they want to go?
    description:  What is the main idea of their traveling?
    season: What is the season they want to go to?
    If place is not specific like Texas, Bangkok, Chiang Rai, it implies null type.
    If description or season is not mentioned, it implies null type.
    answer in JSON format and return only JSON with no other reply or title"""

    extract_template = PromptTemplate.from_template(template)
    return extract_template.format(user_msg=user_msg)

def get_retry_extract_prompt(specification,reference_text,feedback_text):
    # Try extract again
    template = """{specification}
    The above information was misunderstanding.
    Extract the information again with given reference text and feedback text in short and clear.
    Reference Text: "{reference_text}"
    Feedback Text: "{feedback_text}"
    The answer should include
    place: Where do they want to go?
    description:  What is the main idea of their traveling?
    season: What is the season they want to go to?
    If place is not specific like Texas, Bangkok, Chiang Rai, it implies null type.
    If description or season is not mentioned, it implies null type.
    answer in JSON format and return only JSON with no other reply or title"""

    retry_extract_template = PromptTemplate.from_template(template)
    return retry_extract_template.format(specification=specification,
                                         reference_text=reference_text,
                                         feedback_text=feedback_text)

def find_att_prompt_chain():
    find_attraction_name_template = """Given the user specification, it is your job to provide a list of five tourist attractions that match the user need.
    user need: {specification} 
    This is the list of names of the attractions delimited by a comma:"""
    find_attraction_name_prompt_template = PromptTemplate(input_variables = ["specification"], template =  find_attraction_name_template)
    return find_attraction_name_prompt_template

def find_attraction_list_prompt_chain():
    find_attraction_list_template = """Given the list of the attraction names, your task is to describe each of the attraction.
    Each attraction must have a description and the highlights of that attractions within five sentences.
    attraction_name: {attraction_name}
    return in Array JSON format and return only JSON with no other reply or title.
    {format}"""

    find_attraction_list_prompt_template = PromptTemplate(input_variables = ["attraction_name","format"], template = find_attraction_list_template)
    return find_attraction_list_prompt_template
    
