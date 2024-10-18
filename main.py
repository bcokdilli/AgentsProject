from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

memory = MemorySaver()

tavily_search = TavilySearchResults(max_results=3)

tools = [tavily_search]

agent_executor = create_react_agent(
    llm,
    tools,
    checkpointer=memory,
)

config = {"configurable": {"thread_id": "thread-1"}}

if __name__ == "__main__":
    while True:
        message = input("\nEnter a message: ")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=message)]},
            config=config,
        ):
            print(chunk, end="", flush=True)
