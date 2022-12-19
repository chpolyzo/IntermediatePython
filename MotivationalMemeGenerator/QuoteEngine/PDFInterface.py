"""Ingests pdf files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import os
import subprocess

class PDFInterface(IngestorInterface):
    """A pdf ingestion handler class"""

    accepted_files = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses QuoteModel objects of pdf files,
        returning a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'File {path} cannot be processed')
        # temporary file creation aiming to read and save pdftotext output
        temp_file = f".temporary_file_to_delete.txt"
        
        # calling pdftotext tool
        subprocess.run(["pdftotext", "-layout", path, temp_file])
        # iterate through temporary txt file
        with open(temp_file, "r") as infile:
            lines = infile.readlines()
            rows = [line.strip().split("-") for line in lines]
            quotes = [QuoteModel(quote[0], quote[-1]) for quote in rows if (len(quote[0])>0 | len(quote[-1])>0)]
        
        os.remove(temp_file) # Remove the created txt file.
        return quotes