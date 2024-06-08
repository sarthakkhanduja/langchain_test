import requests
import streamlit as st


def get_response(input_text):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post("http://localhost:8079/essay/invoke",
                             headers= headers,
                             json={"input": {"topic": input_text}})
    if response.status_code == 200:
        try:
            print(response.json())
            return response.json()['output']['content']
        except KeyError:
            print(response.json())
            return "Unexpected response format."
    else:
        print(response.json())
        return f"Error: {response.status_code}"


st.title("LangChain API Demo using Gemini Pro")
input_text = st.text_input("Write the topic that you want an essay about")

if input_text:
    st.write(get_response(input_text))