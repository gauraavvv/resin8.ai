import os
import openai 
import tiktoken
from dotenv import load_dotenv, find_dotenv
from typing import Dict
#_ = load_dotenv(find_dotenv()) # read local .env file



openai.api_key  = "sk-y_9Z1HapNzRwJgiaRkKRawrt3-8D2KA6zTFX-3t5GTT3BlbkFJ9hlUe3AqeY6agzHKcUYF9PdNVJbXFYvIDT5osvQ1oA"

def get_completion(prompt, model="gpt-3.5-turbo"):
    

    messages = [{"role": "user", "content": prompt}, {'role':'system', 
 "content":"you are an AI assistant with expertise in providing important features of `description`, `product details`, and `taxonomy` from the json format provided, dont provide html tags "}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output 
    )
    return response.choices[0].message["content"] 

def get_completion_final(prompt, model="gpt-3.5-turbo"):
    

    messages = [{"role": "user", "content": prompt}, {'role':'system', 
 "content":"you are an AI assistant with expertise in providing response in detail in well structured format focuing on `description`, `product details`, and `taxonomy` from the json format provided, dont provide html tags "}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output 
    )
    return response.choices[0].message["content"]


def promptResponse(json_string) -> str:
    
    x=get_completion(json_string,model="gpt-3.5-turbo")
    
    return get_completion_final(x,model="gpt-3.5-turbo")


    


    


