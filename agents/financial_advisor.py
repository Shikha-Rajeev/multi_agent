from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_financials(query):
    gpt4 = ChatOpenAI(model="gpt-4")
    response = gpt4.invoke(query)
    return response
