from PIL import Image
from PIL import ImageDraw, ImageFont
import sys
import os

dir2_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res
 
def create_meme(template_name, text):
    font_size=calculate_font_size(text, ImageFont.truetype('arial', 1), 900)
    img = Image.open(res.image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial', font_size) 
    text_w, text_h=textsize(text, font)
    width, height = img.size

    top_text = text
    bottom_text = ""

    while draw.textlength(top_text, font_size=font_size) > width:
        top_text, last_word = top_text.rsplit(' ', 1)
        bottom_text = last_word + ' ' + bottom_text

    draw_text_with_outline(draw, (0, 0), top_text, font)
    Y_POSN = height - text_h
    X_POSN = 0

    if bottom_text: 
        draw_text_with_outline(draw, (X_POSN, (Y_POSN)), bottom_text, font)

    img.save(res.name_to_save)

def draw_text_with_outline(draw, position, text, font):
    x, y = position
    draw.text((x-1, y), text, font=font, fill="black")
    draw.text((x+1, y), text, font=font, fill="black")
    draw.text((x, y-1), text, font=font, fill="black")
    draw.text((x, y+1), text, font=font, fill="black")
    draw.text(position, text, font=font, fill="white")

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def calculate_font_size(text, font, max_width) -> int:
    font_size = 1
    while font.getlength(text=text) < max_width:
        font_size += 1
        font = ImageFont.truetype('arial', font_size)
    return font_size - 1

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))