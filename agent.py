from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Placeholder tool - नंतर इथे शेतीविषयक टूल्स/प्लगिन जोडता येतील
tools = [
    Tool.from_function(
        name="FarmingGuide",
        description="Provides farming guidance from sowing to harvesting",
        func=lambda x: "हे शेती मार्गदर्शनाचे टूल अजून कार्यरत नाही.",
    )
]

agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)
