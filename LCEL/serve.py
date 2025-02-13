from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv('GROQ_API_KEY')
model=ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key)

from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Translate the following text into {language}"),
        ('user','{text}')
    ]
)
chain=prompt|model|parser

app=FastAPI(
    title="Langchain server",
    version="1.0.",
    description="A simple API for language translation using Langchain."
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)
