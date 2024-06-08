from PIL import Image
from PIL import ImageDraw
import sys
sys.path.append('..')
from res.constants import image_path, name_to_save
 
def create_meme(template_name, text):
    img = Image.open(image_path)
    
    I1 = ImageDraw.Draw(img)
    
    I1.text((100, 100), text=text, fill=(255, 0, 0))
        
    img.save(name_to_save)

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))