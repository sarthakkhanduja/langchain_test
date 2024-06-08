from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Initializing ENV variables
load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initializing the FastAPI
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple FastAPI server for interacting with LLMs"
)

# Initializing the Gemini Pro LLM
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
# llm = Ollama(model="llama2")
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Using a chat prompt template to give the prompt to the LLM
prompt = ChatPromptTemplate.from_template(("You are my writing assistant. I want you to come up with an essay on the "
                                           "topic: '{topic}' within 100 words."))

# Adding the backend route through which this functionality would be called
add_routes(
    app,
    prompt | llm,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8079)
