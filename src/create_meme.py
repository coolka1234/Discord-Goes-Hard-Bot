from PIL import Image
from PIL import ImageDraw
import sys
sys.path.append('..')
from res.constants import image_path, name_to_save
 
img = Image.open(image_path)
 
I1 = ImageDraw.Draw(img)
 
I1.text((28, 36), "nice Car", fill=(255, 0, 0))
 
img.show()
 
img.save(name_to_save)
