from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return JSONKnowledgeSource(file_paths=[filename])
