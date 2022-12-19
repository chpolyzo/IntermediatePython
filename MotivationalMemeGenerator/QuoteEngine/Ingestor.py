"""Interface class wraping up all ingestor interface classes
    for .pdf, .docx, .txt and .csv files each of which has 
    it's own ingestor interface.
    
    Encapsulating Third-Party Libraries
    
    As our system grows and implements more complex code, 
    we'll want a way to organize complex code into a simpler interface. 
    One way of achieving this goal is to encapsulate a more complex
    class or library into a simple class with limited functionality. 
    We'll call this class a strategy object because it represents 
    one possible strategy for achieving an action.
    
    """

from .IngestorInterface import IngestorInterface
from .CSVInterface import CSVInterface
from .DOCXInterface import DOCXInterface
from .TXTInterface import TXTInterface
from .PDFInterface import PDFInterface
from typing import List


class Ingestor(IngestorInterface):
    """
    File manager encapsulation ingestors deciding which Interface ingestor is appropriate.
    It Returns a list of Quote Models as we have working it ouut in the different Interfaces
    for each file type ingestion .
    """

    ingestorInterfaces = [CSVInterface, DOCXInterface, TXTInterface, PDFInterface]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Iterate our differet ingestor Interfaces 
        and run the approprate can_ingest method 
        It returns the list of Quote Models
        """
        for ingestor in cls.ingestorInterfaces:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)