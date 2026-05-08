from crewai import Agent, LLM
import os

def get_agent(tools=None, model_name=None):
    # Fallback to a default if no specific model is passed
    target_model = model_name or os.getenv("MODEL_NAME", "codellama:latest")
    local_llm = LLM(
        model=f"ollama/{target_model}",
        base_url="http://agent-litellm:4000/v1",
        api_key="sk-local-1234"
    )

    return Agent(
        role="Solution Architect",
        goal="Design scalable, modular, and efficient system structures based on requirements.",
        backstory="""You are a veteran systems designer. You focus on the big picture, 
        ensuring that code follows SOLID principles and that the chosen tech stack 
        aligns with the project's long-term scalability and maintenance goals.""",
        llm=local_llm,
        allow_knowledge_retrieval=True,
        tools=tools or [],
        memory=True,
        verbose=True
    )
