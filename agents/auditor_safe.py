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
        role="Cybersecurity Auditor",
        goal="""Review code for vulnerabilities and verify that all file operations are directed toward the allowed '/app/output' directory.""",
        backstory="""You are a strict security officer. You never allow agents to write files
        outside of the designated output folder. You flag any attempt to use absolute paths
        or '..' navigation.""",
        llm=local_llm,
        tools=tools or [],
        memory=True,
        verbose=True
    )
