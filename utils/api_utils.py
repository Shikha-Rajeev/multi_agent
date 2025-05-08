import os
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from anthropic import Anthropic

def get_openai_model():
    return ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

def get_google_model():
    return ChatGoogleGenerativeAI(model="gemini-2.0", api_key=os.getenv("GOOGLE_API_KEY"))

def get_anthropic_model():
    return Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
