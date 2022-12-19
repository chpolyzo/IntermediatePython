"""Ingests docx files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import docx

class DOCXInterface(IngestorInterface):
    """A txt ingestion handler class"""

    accepted_files = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses QuoteModel objects of docx files,
        returning a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'File {path} cannot be processed')
            
        doc = docx.Document(path)
        
        rows = [row.text.split('-') for row in doc.paragraphs if row.text != ""]
        quotes = [QuoteModel(quote[0].strip(), quote[1].strip()) for quote in rows]


        return quotes