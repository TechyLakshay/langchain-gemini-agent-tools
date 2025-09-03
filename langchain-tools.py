from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=api_key
)

# TOOL BINDING
import requests

@tool
def tell_joke() -> str:
    """Get a random programming joke."""
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    response = requests.get(url).json()
    joke = response[0]["setup"] + " " + response[0]["punchline"]
    return joke



tools = [tell_joke]

agent = initialize_agent(
    tools=tools,
    llm = llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

res = agent.run(input("Enter a Topic: "))
print(res)

