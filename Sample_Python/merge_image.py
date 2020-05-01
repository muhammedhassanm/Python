# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:31:42 2020

@author: Muhammed Hassan M
"""


# Combine multiple images into one.
#
# To install the Pillow module on Mac OS X:
#
# $ xcode-select --install
# $ brew install libtiff libjpeg webp little-cms2
# $ pip install Pillow
#

from __future__ import print_function
import os

from PIL import Image

files = [
  'C:/Users/Muhammed Hassan M/Desktop/Untitled.png',
  'C:/Users/Muhammed Hassan M/Desktop/Untitled1.png'
  ]

result = Image.new("RGB", (600,800))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((400, 400), Image.ANTIALIAS)
  x = index // 2 * 400
  y = index % 2 * 400
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('~/image.jpg'))