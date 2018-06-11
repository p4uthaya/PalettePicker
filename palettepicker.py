# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:52:13 2018

@author: Prabha
"""
import colorgram
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

im = Image.open("Thalapathi - 1.30.25.png")
print(im.format, im.size, im.mode)

img = np.array(im)

plt.figure()
plt.imshow(img)


# Extract 6 colors from an image.
colors = colorgram.extract('Thalapathi - 1.30.25.png',6)
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

first_color = colors[0]

rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# ___ understanding colorgram ___
# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
#red = rgb[0]
#red = rgb.r
#saturation = hsl[1]
#saturation = hsl.s
#colors.sort(key=lambda c: c.hsl.h)
#
#pall = np.array([[colors[1].rgb.r,colors[1].rgb.g,colors[1].rgb.b]])
#print(pall)
#
#print (colors)

# array of 6 colours 
pal = np.zeros((6,3),dtype=np.uint8) # dtype makes it a number btw 0 and 255
#print(pal)

for i in range(6):
    pal[i] = [colors[i].rgb.r,colors[i].rgb.g,colors[i].rgb.b]

print (pal)
indx =np.array([[0,1,2,3,4,5]])

plt.figure()
io.imshow(pal[indx])

def pallate (file_name,num_of_col):
    name = file_name
    no = num_of_col
    
    # printing the image
    im = Image.open(name)
    img = np.array(im)

    plt.figure()
    plt.imshow(img)
    
    # finding colour objects via colourgram
    colors = colorgram.extract(name, no)
    
    # making pallate with RGB values 
    pal = np.zeros((no,3), dtype=np.uint8) # dtype makes it a number btw 0 and 255
    
    for i in range(no):
        pal[i] = [colors[i].rgb.r,colors[i].rgb.g,colors[i].rgb.b]
    indx = np.array([range(no)]) # indices for pallete colourbar 
    #print(indx)
    plt.figure()
    io.imshow(pal[indx])
    
#pallate('Kuttrame Thandanai - 1.11.40.png',6)

#pallate('Thalapathi - 0.51.36.png',6)

pallate('Thalapathi - 1.29.05.png',6)

pallate('Thalapathi - 1.00.34.png',6)

#pallate('DSC_0020.jpg',9)

    
#pallate('red.jpg',2)
