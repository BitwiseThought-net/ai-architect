from crewai.knowledge.source.xml_knowledge_source import XMLKnowledgeSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return XMLKnowledgeSource(file_paths=[filename])
