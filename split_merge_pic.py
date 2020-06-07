#!/usr/bin/python

#############################################################
# Des:      Split or merge picture.
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     26/5/2020
#############################################################

from PIL import Image

pic1 = Image.open(r"D:\Life-File\picture\git.jpg")
pic1.show()

r, g, b = pic1.split()
print(r.size, r.mode)
pic2 = Image.merge('RGB', (r, g, r))
pic2.show()