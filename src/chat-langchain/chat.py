from typing import Any
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.llms import llamacpp
from langchain.llms import Ollama

class SimpleChat:
    def __init__(self, openai_api_base, openai_api_key, temperature, chat_messages, ):
        self.llm = ChatOpenAI(
            openai_api_base=openai_api_base, 
            openai_api_key=openai_api_key,
            temperature=temperature,
        )
        self.chat_messages = chat_messages
        
    def __call__(self, message_dict) -> str:
        prompt = ChatPromptTemplate.from_messages(self.chat_messages)  
        chain = prompt | self.llm
        rt = chain.invoke(message_dict)
        return rt.content
