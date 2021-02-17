#!/usr/bin/python

#############################################################
# Des:      Regional a picture.
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     26/5/2020
#############################################################

from PIL import Image

pic = Image.open(r"D:\Life-File\picture\git.jpg")
box = pic.copy()
box = (80, 80, 380, 380)
region = pic.crop(box)
region.show()