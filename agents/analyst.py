from crewai import Agent, LLM
import os

def get_agent(tools=None, model_name=None):
    # Fallback to a default if no specific model is passed
    target_model = model_name or os.getenv("MODEL_NAME", "llama3:latest")
    local_llm = LLM(
        model=f"ollama/{target_model}",
        base_url="http://agent-litellm:4000/v1",
        api_key="sk-local-1234"
    )

    return Agent(
        role="Data Insights Analyst",
        goal="Extract, clean, and interpret patterns from structured and unstructured data sources.",
        backstory="""You are an expert at finding the story within the data. Whether it is a 
        massive CSV or a folder full of logs, you provide statistical summaries and 
        actionable insights to guide the team's decisions.""",
        llm=local_llm,
        allow_knowledge_retrieval=True,
        tools=tools or [],
        memory=True,
        verbose=True
    )
