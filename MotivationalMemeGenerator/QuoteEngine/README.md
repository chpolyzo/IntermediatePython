Quote Engine
The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

"This is a quote body" - Author
This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

Quote Format
Example quotes are provided in a variety of files. Take a moment to review the file formats in ./_data/SimpleLines and ./_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.

Ingestors
An abstract base class, IngestorInterface should define two methods with the following class method signatures:

def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).

A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

Installing Xpdf
Xpdf may not be installed on your local machine. If this is the case, you can install it using the open source XpdfReader utility. Here are some tips for installing xpdf on different operating systems:

For Mac, we suggest that you use Homebrew:
If you don't already have it, install use the command provided here to install Homebrew. After installing, read the last few lines that it outputs in your CLI—it may provide additional commands that you can run to add Homebrew to PATH.
Once Homebrew is installed, simply run brew install xpdf in the terminal.
For Windows, you'll need to:
Download the Windows command-line tools from the xpdf website.
Unzip the files in a location of your choice.
Get the full file path to the folder named bin32 (if you have a 32-bit machine) or bin64 (if you have a 64-bit machine).
Add this path to the Path environment variable. This will allow you to use the xpdf command from the command line. If you've never done this before, check out this Stack Overflow post on how to add a folder to the Path environment variable.
For Linux, you can use Homebrew (as shown above for Mac) or apt-get to install (simply enter sudo apt-get install -y xpdf in your command line interface).
⚠️ Note that there is also a pdftotext library available from PyPi. Do not use this PyPi library. For this project, the goal is to use Xpdf and demonstrate your understanding of the subprocess module.