"""
Python module creation in a directory called QuoteEngine including __init__.py
"""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

"""Import all Ingestors and make them available upon package import."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVInterface import CSVInterface
from .DOCXInterface import DOCXInterface
from .TXTInterface import TXTInterface
from .PDFInterface import PDFInterface
from .Ingestor import Ingestor