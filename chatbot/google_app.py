from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a professional chef. Your job is to provide the best possible recipe for the ingredients available with the user (separated by a comma). The user prefers Indian cuisine,  and you can assume the user has spices available."
                   "that the user might have"),
        ("user", "List of Ingredients: {question}")
    ]
)

# filled_prompt = prompt.format(question="What is the weather going to be if it rained yesterday, but has been sunny since morning, in the summer season?")
# print(filled_prompt)

# StreamLit Framework

st.title('Kitchen AI with Google Gemini Pro (By, Sarthak Khanduja)')
input_text = st.text_input("Please enter the list of ingredients separated by a comma")

# Ollama LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))