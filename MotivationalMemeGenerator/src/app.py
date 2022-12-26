import random
import os
import requests
import string
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')

def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes_lists = [Ingestor.parse(q_list) for q_list in  quote_files]
    quotes = [q for sublist in quotes_lists for q in sublist]
    print(f'These are the quotes: {quotes}')
    
    
    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, f) for f in os.listdir(images_path) if f.endswith(".jpg")]
    print(f'These are the images: {imgs}')
   
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.create_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """


    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    
    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    
    # test img_url
    # https://www.dogstrust.org.uk/images/1440x1080/assets/2022-07/Buster_germanshepherd_outdoors_leeds_dogstrust.jpg
    response = requests.get(img_url, allow_redirects=True)
    
    tmp = os.path.join('./static/', 
                       ''.join(random.choice(string.ascii_letters) for x in range(15)) + '.png')
    print(f'this is temp post {tmp}')
    img = open(tmp, 'wb').write(response.content)
    path = meme.create_meme(tmp, body, author)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
