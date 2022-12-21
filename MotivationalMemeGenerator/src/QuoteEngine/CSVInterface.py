"""Ingests csv files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import pandas as pd


class CSVInterface(IngestorInterface):
    """A class that handles the ingestion of csv files."""

    accepted_files = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse QuoteModel obj of csv files and return a list of them."""
        if not cls.can_ingest(path):
            raise ValueError(f'File {path} cannot be processed')

        
        df = pd.read_csv(path)
        quotes = [QuoteModel(df.loc[idx, 'body'], df.loc[idx, 'author']) for idx in range(len(df))]
        return quotes