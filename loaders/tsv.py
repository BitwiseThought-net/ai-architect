from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return TextFileKnowledgeSource(file_paths=[filename])
