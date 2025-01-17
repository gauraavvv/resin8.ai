import os as os
import openai 
import tiktoken
from dotenv import load_dotenv, find_dotenv
from typing import Dict

_ = load_dotenv(find_dotenv())  # read local .env fil
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    
    try:
     messages = [{"role": "user", "content": prompt}, {'role':'system', 
 "content":"you are an AI assistant with expertise in providing important features of `description`, `product details`, and `taxonomy` from the json format provided, dont provide html tags "}]
     response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output 
    )
     return response.choices[0].message["content"] 
    except openai.error.AuthenticationError:
        return "Authentication failed: API key is invalid or missing."

def get_completion_final(prompt, model="gpt-3.5-turbo"):
    

    messages = [{"role": "user", "content": prompt}, {'role':'system', 
 "content":"you are an AI assistant with expertise in providing response in detail of all the components provided in well structured format focuing on `description`, `product details`, and `taxonomy` from the json format provided, dont provide html tags "}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output 
    )
    return response.choices[0].message["content"]


def promptResponse(json_string) -> str:
    
    x=get_completion(json_string,model="gpt-3.5-turbo")
    
    return get_completion_final(x,model="gpt-3.5-turbo")


    


    


