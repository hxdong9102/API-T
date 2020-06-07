#!/usr/bin/python

#############################################################
# Des:      Rize or rotate a picture.
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     26/5/2020
#############################################################

from PIL import Image

pic = Image.open(r"D:\Life-File\picture\git.jpg")

out = pic.resize((300, 300))
out.show()
# Contrarotate 45 degree.
out = pic.rotate(45)     
out.show()

out = pic.transpose(Image.FLIP_LEFT_RIGHT)
out.show()
out = pic.transpose(Image.FLIP_TOP_BOTTOM)
out.show()

out = pic.transpose(Image.ROTATE_90)
out.show()
out = pic.transpose(Image.ROTATE_180)
out.show()
out = pic.transpose(Image.ROTATE_270)
out.show()
