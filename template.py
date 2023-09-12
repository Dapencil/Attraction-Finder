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

def get_find_att_prompt(specification):
    # Find Att
    template = """{specification}
    
    Provide a list of five tourist attractions that match the above need.
    then return in Array JSON format and return only JSON with no other reply or title.
    
    {json_format}"""
    
    format_att_instruction = """{
        name: name of the attraction,
        description: illustrate about the attraction in 4 - 5 sentence,
        highlights : three descriptive highlights of the attraction
        }"""
    find_attraction_template = PromptTemplate.from_template(template)
    return find_attraction_template.format(specification=specification,
                                           json_format=format_att_instruction)