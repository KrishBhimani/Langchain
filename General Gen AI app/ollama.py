import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2']="true"

prompt=ChatPromptTemplate(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{input}")
    ]
)

st.title("Langchan Demo with Llama3.2")
input_text=st.text_input("What question you have in mind?")

llm=Ollama(model="llama3.2")
parser=StrOutputParser()
chain=prompt|llm|parser

if input_text:
    st.write(chain.invoke({"input":input_text}))
