#!/usr/bin/python3

import sys
import random
from PIL import Image, ImageDraw

default_resolution = {1920, 1080}

im = Image.new('RGB', (500,500))

draw = ImageDraw.Draw(im)
#draw.line((0,0) + im.size, fill = 128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)

for i in range(0,)


del draw

im.save('out.png', "PNG")



"""
class WallGen:
	def __init__(self):
		pass
"""



