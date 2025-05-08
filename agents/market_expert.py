from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_market_trends(query):
    claude = ChatOpenAI(model="claude-3")
    response = claude.invoke(query)
    return response
