"""
This is the Meme Engine module. 
The ImageGenerator class creates 
the final meme which includes both picture and text
"""

from QuoteEngine.QuoteModel import QuoteModel
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import string
import textwrap
import os

class MemeEngine(object):
    """
    ImageGenerator takes as input
    input:the output directory specified
    method create_meme opens image and adds a quote inside the resized image 500 x 500
    es. meme = MemeEngine("./meme_directory")
    output_path = meme.create_meme("path to image", "body of quote", "author of quote")
    Pictures with the relative quotes are stored in the meme_directory.
    """

    def __init__(self, output_directory):
        self.output_directory = output_directory

    def create_meme(self, image, body, author, width=500) -> str:
        try:
            img = Image.open(image)
            print("Image Opened")
            img_aspect_ratio = img.width/img.height
            mm_width, mm_height = 500, int(500*img_aspect_ratio)
            resized_img = img.resize((mm_width, mm_height))
            print("Image resized")
            
            # take the string overide
            quote = QuoteModel(body, author).__str__()
            # wrap the quote inside the picture
            quote_printout = textwrap.fill(quote, 50) if len(quote) > 50 else quote
            
            # set coordinates in the picture
            x = int(mm_width/16)
            y = int(mm_height/16)
            
            # draw the entire meme (picture and text together)
            draw_meme = ImageDraw.Draw(resized_img)
            draw_meme.text((x, y), text=quote_printout, font=ImageFont.truetype("verdana.ttf", 15))
            
            # create the final path
            output_path = os.path.join(self.output_directory, 
                                       ''.join(random.choice(string.ascii_letters) for x in range(15)) + '.png')
            print(output_path)
            # save meme
            resized_img.save(output_path)
            print("Image saved")
            return output_path
        
        except Exception as e:
            raise Exception(e)