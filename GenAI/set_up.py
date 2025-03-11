from langchain_openai import ChatOpenAI
import openai
openai.api_key = 'sk-proj-Ylo6jyEE3fDGbhe-Hq'

llm = ChatOpenAI()

llm.invoke('Hello?')