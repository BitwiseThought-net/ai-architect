from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return CSVKnowledgeSource(file_paths=[filename])
