import os
import subprocess
import requests
from crewai import (
    Agent as NativeAgent,
    Task as NativeTask,
    Crew as NativeCrew,
    Process as NativeProcess,
    LLM as NativeLLM
)
from crewai.tools import tool as native_tool, BaseTool # FIXED: Added BaseTool import

# Import only the stable core file interaction tools
from crewai_tools import (
    FileReadTool as NativeFileReadTool,
    FileWriterTool as NativeFileWriterTool
)

# Import explicit knowledge source classes utilized by your loaders/ directory
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# --- CORE BINDINGS ---
Agent = NativeAgent
Task = NativeTask
Crew = NativeCrew
Process = NativeProcess
LLM = NativeLLM
tool = native_tool

# --- TOOL BINDINGS ---
FileReadTool = NativeFileReadTool
FileWriterTool = NativeFileWriterTool

# --- INLINE SECURE SHELL EXECUTION FALLBACK ---
# FIXED: Subclassed BaseTool to satisfy Pydantic structure compilation constraints
class NativeShellInterpreter(BaseTool):
    name: str = "terminal_execution_tool"
    description: str = "Executes arbitrary shell commands inside the application workspace container environment."

    def _run(self, command: str) -> str:
        """Executes terminal parameters safely and returns output packages."""
        try:
            res = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )
            out = res.stdout if res.stdout else ""
            err = res.stderr if res.stderr else ""
            return f"Stdout: {out}\nStderr: {err}"
        except Exception as e:
            return f"Execution Failed: {str(e)}"

EXECTool = NativeShellInterpreter

# --- INLINE SECURE SEARCH FALLBACK ---
# FIXED: Subclassed BaseTool to satisfy Pydantic structure compilation constraints
class NativeDuckDuckGoSearch(BaseTool):
    name: str = "duckduckgo_search"
    description: str = "Search the web for real-time technical documentation, requirements, and standards."

    def _run(self, query: str) -> str:
        """Executes an unauthenticated search query pass against the public index."""
        url = "duckduckgo.com"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"}
        try:
            response = requests.post(url, data={"q": query}, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text[:8000]
            return f"⚠️ Search index rejected query with status: {response.status_code}"
        except Exception as e:
            return f"❌ Search execution failed: {str(e)}"

DuckDuckGoSearchTool = NativeDuckDuckGoSearch

# --- KNOWLEDGE LOADER MAPPINGS ---
class Knowledge:
    CSV = CSVKnowledgeSource
    Docling = CrewDoclingSource
    JSON = JSONKnowledgeSource
    Excel = ExcelKnowledgeSource
    TextFile = TextFileKnowledgeSource
    XML = CrewDoclingSource

