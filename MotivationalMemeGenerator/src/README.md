# Meme Generator
## About the project
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, 
including an image with an overlaid quote.
## Building Packages
1. [Pandas](https://pandas.pydata.org/)
2. [Python-Pillow](https://python-pillow.org/)
3. [Flask](https://flask.palletsprojects.com/en/2.2.x/)
## Tasks
There is provided some code and data to get started. Sample quotes and images of Xander the pup in src/_data/.
There's also a basic flask server which will consume your modules and make it usable through a web interface. 
The main code for this flask service is in app.py, 
templates are in templates/ and generated images should be saved to static/. 
Students need to install the flask dependency with pip install flask and you run the server with python3 app.py.

## The application students build must:
Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
Load, manipulate, and save images.
Accept dynamic user input through a command-line tool and a web service. 
This emulates the kind of work you’ll encounter as a full stack developer.
This project will give you a hands-on opportunity to practice what you've learned in this course, such as:

Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
DRY (don’t repeat yourself) principles of class and method design.
Working with modules and packages in Python.

## Quote Engine
The `Quote Engine` module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

`"This is a quote body" - Author`
This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

### Quote Format
Example quotes are provided in a variety of files. Take a moment to review the file formats in ./_data/SimpleLines and ./_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.

### Ingestors
An abstract base class, IngestorInterface should define two methods with the following class method signatures:

`def can_ingest(cls, path: str) -> boolean`

`def parse(cls, path: str) -> List[QuoteModel]`

Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).

A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

### Installing Xpdf
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

## Meme Engine Module
The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.

## Package your Application
Larger, complex systems need an interface for users to interact with. We'll package the project as a command line tool and as a simple web service.

### Create a Command-Line Interface tool
The project contains a simple cli app starter code in meme.py. This file contains @TODO tasks for you to complete. The utility can be run from the terminal by invoking python3 meme.py

The script must take three optional CLI arguments:
```
--body a string quote body
--author a string quote author
--path an image path
```
The script returns a path to a generated image. If any argument is not defined, a random selection is used.

### Complete the Flask app
The project contains a flask app starter code in app.py. This file contains @TODO tasks for you to complete.

The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.

It uses the requests package to fetch an image from a user submitted URL.

The flask server must run with no errors
