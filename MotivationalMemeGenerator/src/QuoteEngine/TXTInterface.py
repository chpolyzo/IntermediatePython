"""Ingests txt files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class TXTInterface(IngestorInterface):
    """A txt ingestion handler class """

    accepted_files = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses QuoteModel objects of txt files,
        returning a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'File {path} cannot be processed')

        with open(path, "r", encoding="utf-8-sig") as infile:
            filelines = infile.readlines()
        
        rows = [row.replace("\n", "").split("-") for row in filelines]
        quotes = [QuoteModel(quote[0].strip(), quote[1].strip()) for quote in rows]
        return quotes