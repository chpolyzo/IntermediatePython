"""An abstract base class, IngestorInterface defining two methods"""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """
    At a high level, an interface acts as a blueprint for designing classes. 
    Like classes, interfaces define methods. Unlike classes, these methods are abstract. 
    An abstract method is one that the interface simply defines. 
    It doesn't implement the methods.
    
    In this interface we define two abstract methods:
    
    def can_ingest(cls, path: str) -> boolean
    def parse(cls, path: str) -> List[QuoteModel]
    
    These methods will be then be implemented by classes
    """
    
    accepted_files = []
    
    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        """
        Boolean decision maker abstract method checking 
        if a certain file extension is permitted
        given our app structure. 
        We can only accept .txt, .docx, .pdf and .csv files.
        """
        flag = path.split('.')[-1] in cls.accepted_files
        return flag
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Abstract method, overriding implementantions
        for each quote in a parsed file.
        
        """
        pass