from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import SequentialChain
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import json
from template import (get_extract_prompt,get_retry_extract_prompt,find_att_prompt_chain,find_attraction_list_prompt_chain)

class MyAgent:

    def __init__(self,api_key,model_name):
        self.api_key = api_key
        self.chat = ChatOpenAI(openai_api_key=api_key,temperature = 0.0, model = model_name)

    def extract_info(self,user_msg):
       prompt = get_extract_prompt(user_msg)
       specification_str = self.chat([HumanMessage(content=prompt)]).content
       specification = json.loads(specification_str)
       return specification
    
    def retry_extract(self,specification,reference_text,feedback_text):
        prompt = get_retry_extract_prompt(specification=specification,
                                          reference_text=reference_text,
                                          feedback_text=feedback_text)
        specification_str = self.chat([HumanMessage(content=prompt)]).content
        specification = json.loads(specification_str)
        return specification

    def find_atts_chain(self,spec_msg):    
        attraction_name_chain = LLMChain(llm = self.chat, prompt = find_att_prompt_chain(), output_key = "attraction_name")
        attraction_list_chain = LLMChain(llm = self.chat, prompt = find_attraction_list_prompt_chain(),  output_key = "attraction_list")
        overall_chain = SequentialChain(
            chains=[attraction_name_chain, attraction_list_chain],
            input_variables=["specification","format"],
        output_variables=["attraction_name", "attraction_list"],verbose = True)
        format = """{
        "name": name of the attraction,
        "description": illustrate the attraction within five sentences,
        "highlights" : three descriptive highlights of the attraction
        }"""
        result = overall_chain({"specification":spec_msg,"format":format})
        att_list = json.loads(result['attraction_list'])
        return att_list
    
    