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
        role="Quality Assurance Engineer",
        goal="Identify edge cases and write automated unit/integration tests to ensure code reliability.",
        backstory="""You are a rigorous QA specialist. You believe that if it isn't tested, 
        it's broken. You excel at writing Python 'pytest' suites and finding logical 
        flaws in newly written code before it hits production.""",
        llm=local_llm,
        allow_knowledge_retrieval=True,
        tools=tools or [],
        memory=True,
        verbose=True
    )
