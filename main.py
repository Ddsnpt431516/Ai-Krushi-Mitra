from fastapi import FastAPI
from langchain_core.messages import AIMessage, HumanMessage
from langserve import add_routes
from agent import agent_executor

app = FastAPI()
add_routes(
    app,
    agent_executor,
    path="/agent"
)

@app.get("/")
async def root():
    return {"message": "AI-Krushi-Mitra is running"}
