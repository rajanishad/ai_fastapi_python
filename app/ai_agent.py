from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.7, model="gpt-3.5-turbo")

def ask_ai(question: str) -> str:
    response = llm.invoke([HumanMessage(content=question)])
    return response.content
