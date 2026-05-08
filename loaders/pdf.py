from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return PDFKnowledgeSource(file_paths=[filename])
