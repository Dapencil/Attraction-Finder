from langchain.llms import OpenAI
import json
from template import (get_extract_prompt,get_find_att_prompt,get_retry_extract_prompt)

class MyAgent:

    def __init__(self,api_key,model_name):
        self.api_key = api_key
        self.llm = OpenAI(model_name=model_name,openai_api_key=api_key)

    def extract_info(self,user_msg):
       prompt = get_extract_prompt(user_msg)
       specification_str = self.llm(prompt)
       specification = json.loads(specification_str)
       return specification
    
    def retry_extract(self,specification,reference_text,feedback_text):
        prompt = get_retry_extract_prompt(specification=specification,
                                          reference_text=reference_text,
                                          feedback_text=feedback_text)
        specification_str = self.llm(prompt)
        specification = json.loads(specification_str)
        return specification

    def find_atts(self,spec_msg):
       prompt = get_find_att_prompt(specification=spec_msg)
       att_list_str = self.llm(prompt)
       att_list = json.loads(att_list_str)
       return att_list