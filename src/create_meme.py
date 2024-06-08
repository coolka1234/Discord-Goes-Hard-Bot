from PIL import Image
from PIL import ImageDraw, ImageFont
import sys
import os

dir2_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res
 
def create_meme(template_name, text):
    img = Image.open(res.image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial', 32)  # choose a suitable font and size

    width, height = img.size

    # Split the text into two parts
    top_text = text
    bottom_text = ""

    while draw.textlength(top_text, font_size=32) > width:
        top_text, last_word = top_text.rsplit(' ', 1)
        bottom_text = last_word + ' ' + bottom_text

    # Draw the top text
    draw_text_with_outline(draw, (0, 0), top_text, font)

    # Draw the bottom text
    print(height)
    if bottom_text:  # if there is any text left
        draw_text_with_outline(draw, (0, -(height - draw.textlength(bottom_text, font_size=32))), bottom_text, font)

    img.save(res.name_to_save)

def draw_text_with_outline(draw, position, text, font):
    x, y = position
    draw.text((x-1, y), text, font=font, fill="black")
    draw.text((x+1, y), text, font=font, fill="black")
    draw.text((x, y-1), text, font=font, fill="black")
    draw.text((x, y+1), text, font=font, fill="black")
    draw.text(position, text, font=font, fill="white")

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))