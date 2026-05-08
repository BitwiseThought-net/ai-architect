from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
import os

def get_source(file_path):
    filename = os.path.basename(file_path)
    return CrewDoclingSource(file_paths=[filename])
