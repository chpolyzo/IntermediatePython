
"""
Simple QuoteModel implementation class to encapsulate the body and author
"""
class QuoteModel:
    """
    Implementation class to encapsulate a quote body and a quote author.
    The purpose of our quote generator contains a body and an author
    """

    def __init__(self, body: str, author: str):
        """Create a simple model using a quote author and a quote body."""
        self.author = str(author)
        self.body = str(body)

    def __str__(self):
        """Override method representing the QuoteModel class objects as a string"""
        return f"{self.body} \n Quote by {self.author}"

    def __repr__(self):
        """Override method used to represent a class's objects as a string"""
        return f"Quote Model Author: {self.author}, Quote Model body: {self.body}"
  