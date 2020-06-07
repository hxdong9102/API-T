#!/usr/bin/python

#############################################################
# Des:      Show or save a picture.
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     26/5/2020
#############################################################


from PIL import Image

pic = Image.open(r"D:\Life-File\picture\git.jpg")
pic.show()
print(pic.format, pic.size, pic.mode)
pic.save('copy.png')
