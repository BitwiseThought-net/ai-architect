from crewai import Agent, LLM
import os

def get_agent(tools=None, model_name=None):
    # Fallback to a default if no specific model is passed
    target_model = model_name or os.getenv("MODEL_NAME", "mistral:latest")
    local_llm = LLM(
        model=f"ollama/{target_model}",
        base_url="http://agent-litellm:4000/v1",
        api_key="sk-local-1234"
    )

    return Agent(
        role="System Librarian",
        goal="Ensure all local documentation is properly indexed and available for the team.",
        backstory="""You are the gatekeeper of knowledge. You scan the knowledge directory 
        for new materials, organize them, and ensure the team is working with the most up-to-date data.""",
        llm=local_llm,
        allow_knowledge_retrieval=True,
        tools=tools or [],
        memory=True,
        verbose=True
    )
