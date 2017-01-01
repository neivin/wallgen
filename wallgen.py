import sys
import random
from PIL import Image, ImageDraw

im = Image.new('RGB', (500,500), color=0)

draw = ImageDraw.Draw(im)
draw.line((0,0) + im.size, fill = 128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

im.save('out', "PNG")
class ColorfulWall:
:wq

