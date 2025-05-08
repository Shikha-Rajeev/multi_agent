from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_business_kpis(query):
    gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = gemini.invoke(query)
    return response
