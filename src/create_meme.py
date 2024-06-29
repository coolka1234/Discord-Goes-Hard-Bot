from math import log
from PIL import Image
from PIL import ImageDraw, ImageFont
import sys
import os
import logging

dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res
log_path=os.path.abspath('./docs/bot.log')
logging.basicConfig(level=logging.INFO, filename=log_path, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def create_meme(template_number, text) -> None:
    img = Image.open(res.image_path[template_number])
    width, height = img.size
    # width=int(width*0.90)
    max_width = width*2 # 
    font_size=calculate_font_size(text, ImageFont.truetype('arial', 1), max_width* res.scale_factor) # wont work on linux, hast to be installed
    if font_size == 0:
        return     
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial', font_size) 
    text_w, text_h=textsize(text, font)
    logging.info(f"Drawing: text_w: {text_w}, text_h: {text_h}")
    logging.info(f"Drawing: width: {width}, height: {height}")
    bottom_text = ""

    while draw.textlength(top_text, font_size=font_size) > width:
        top_text, last_word = top_text.rsplit(' ', 1)
        bottom_text = last_word + ' ' + bottom_text
    top_text = ' ' + top_text + ' '
    bottom_text = ' ' + bottom_text + ' '
    top_text_w, _ = textsize(top_text, font)
    top_text_x=(width - top_text_w) / 2
    top_text_y=height-(height*res.scale_factor)

    logging.info(f"Drawing: top_text_x: {top_text_x}, top_text_y: {top_text_y}, top_text: {top_text}")
    draw_text_with_outline(draw, (top_text_x, top_text_y), top_text, font)

    font_size=calculate_font_size(bottom_text, ImageFont.truetype('arial', 1), width* res.scale_factor)
    font = ImageFont.truetype('arial', font_size)
    bottom_text_w, _ = textsize(bottom_text, font)


    Y_POSN = height - text_h
    Y_POSN = Y_POSN *res.scale_factor
    X_POSN = (width - bottom_text_w) / 2

    if bottom_text:
        X_POSN = (width - bottom_text_w) / 2
        logging.info(f"Drawing: X_POSN: {X_POSN}, Y_POSN: {Y_POSN}, bottom_text: {bottom_text}, bottom_text_w: {bottom_text_w}") 
        draw_text_with_outline(draw, (X_POSN, (Y_POSN)), bottom_text, font)

    img.save(res.name_to_save)

def draw_text_with_outline(draw, position, text, font):
    x, y = position
    draw.text((x-1, y), text, font=font, fill="black")
    draw.text((x+1, y), text, font=font, fill="black")
    draw.text((x, y-1), text, font=font, fill="black")
    draw.text((x, y+1), text, font=font, fill="black")
    draw.text(position, text, font=font, fill="white")

def textsize(text, font) -> tuple[int, int]:
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