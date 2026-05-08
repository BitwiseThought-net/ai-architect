from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return ExcelKnowledgeSource(file_paths=[filename])
